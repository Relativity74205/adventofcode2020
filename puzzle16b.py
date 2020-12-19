from pathlib import Path
from typing import Iterator, Dict
from functools import reduce
from operator import mul
from collections import Counter
from copy import deepcopy

with open(Path(__file__).parent / "data" / "puzzle16.txt", "r") as f:
    raw_data = f.read().splitlines()


ranges = {}
for row in raw_data:
    if row == '':
        break
    else:
        field = row.split(':')[0]
        all_values = row.split(':')[1]
        value_range1 = all_values.split(' or ')[0]
        value_range2 = all_values.split(' or ')[1]
        ranges[field] = {'min1': int(value_range1.split('-')[0]),
                         'max1': int(value_range1.split('-')[1]),
                         'min2': int(value_range2.split('-')[0]),
                         'max2': int(value_range2.split('-')[1]),
                         }
your_ticket_row = int([i for i, row in enumerate(raw_data) if row.startswith('your ticket')][0]) + 1
nearby_ticket_rows = int([i for i, row in enumerate(raw_data) if row.startswith('nearby tickets')][0]) + 1

your_ticket_data = raw_data[your_ticket_row]
your_ticket_data_list = list(map(int, your_ticket_data.split(',')))

nearby_ticket_data = [row for row in raw_data[nearby_ticket_rows:]]


def check_value(value_range: Dict, value: int) -> int:
    if (value_range['min1'] <= value <= value_range['max1']
            or value_range['min2'] <= value <= value_range['max2']):
        return True
    return False


def check_field(value: int) -> int:
    for value_range in ranges.values():
        if (value_range['min1'] <= value <= value_range['max1']
                or value_range['min2'] <= value <= value_range['max2']):
            return 0
    return value


def validate_ticket(values: Iterator[int]) -> int:
    fields = [check_field(value) for value in values]

    return sum(fields)


def valid_possibility(col: int, possibility: str):
    possibility_range = ranges[possibility]
    for valid_ticket in valid_tickets:
        ticket_value = valid_ticket[col]
        if not check_value(possibility_range, ticket_value):
            return False

    return True


def remove_possibilities(possibilities):
    possibilities_copy = deepcopy(possibilities)
    for col, fields in possibilities.items():
        for pos in fields:
            valid = valid_possibility(col, pos)
            if valid is False:
                possibilities_copy[col].remove(pos)

    return possibilities_copy


tickets_check = {i: validate_ticket(map(int, ticket.split(','))) for i, ticket in enumerate(nearby_ticket_data)}
valid_tickets = [list(map(int, ticket.split(','))) for error_rate, ticket in zip(tickets_check.values(), nearby_ticket_data) if error_rate == 0]

field_possibilities = {pos: list(ranges.keys()) for pos in range(len(your_ticket_data.split(',')))}
field_possibilities_cleaned = remove_possibilities(field_possibilities)

# for col, fields in field_possibilities_cleaned.items():
#     for field in fields:
#         valid = valid_possibility(col, field)
#         if valid is False:
#             print(col, field)


def get_shortest_col(sol) -> int:
    shortest_col, shortest_col_len = -1, 21
    for col, pos in sol.items():
        col_len = len(pos)
        if col_len == 1:
            continue

        if col_len < shortest_col_len:
            shortest_col, shortest_col_len = col, col_len

    return shortest_col


def strip_possibilities(sol):
    for col in sol.keys():
        if len(sol[col]) == 1:
            for current_col, pos in sol.items():
                if len(sol[col]) == 0 or current_col == col:
                    continue

                try:
                    pos.remove(sol[col][0])
                except ValueError:
                    pass

    return sol


def check_all_one(sol) -> bool:
    all_one = [True if len(pos) == 1 else False for pos in sol.values()]

    return all(all_one)


def check_any_zero(sol) -> bool:
    any_zero = [True if len(pos) == 0 else False for pos in sol.values()]
    return any(any_zero)


def check_valid_solution(sol) -> bool:
    any_one_non_valid = [valid_possibility(col, field[0])
                             for col, field in sol.items()
                             if len(field) == 1]

    return all(any_one_non_valid)


def solve(sol):
    if check_all_one(sol):
        if check_valid_solution(sol):
            return sol
        else:
            return None

    sol_copy = deepcopy(sol)
    shortest_col = get_shortest_col(sol_copy)
    field_candidates = sol[shortest_col].copy()
    for field in field_candidates:
        sol_copy[shortest_col] = [field]
        sol_copy = strip_possibilities(sol_copy)
        if not check_any_zero(sol_copy):
            sol_candidate = solve(sol_copy)
            if sol_candidate is not None:
                return sol_candidate

        # sol[shortest_col].remove(field)
        sol_copy = deepcopy(sol)

    return None


final_solution = solve(field_possibilities_cleaned)
departure_cols = [col for col, field in final_solution.items() if field[0].startswith('departure')]

final_final_solution = reduce(mul, [your_ticket_data_list[col] for col in departure_cols])
print(f'{final_final_solution=}')
