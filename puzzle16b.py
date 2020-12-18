from pathlib import Path
from typing import Iterator, Dict
from functools import reduce
from operator import add
from collections import Counter

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


def valid_possibility(col, possibility):
    possibility_range = ranges[possibility]
    for valid_ticket in valid_tickets:
        ticket_value = valid_ticket[col]
        if not check_value(possibility_range, ticket_value):
            return False

    return True


tickets_check = {i: validate_ticket(map(int, ticket.split(','))) for i, ticket in enumerate(nearby_ticket_data)}
valid_tickets = [list(map(int, ticket.split(','))) for error_rate, ticket in zip(tickets_check.values(), nearby_ticket_data) if error_rate == 0]

field_possibilities = {pos: list(ranges.keys()) for pos in range(len(your_ticket_data.split(',')))}


def remove_possibilities(possibilities):
    possibilities_copy = possibilities.copy()
    for col, col_possibilities in possibilities.items():
        for possibility in col_possibilities:
            if not valid_possibility(col, possibility):
                possibilities_copy[col].remove(possibility)

    return possibilities_copy


def check_only_one():
    pass


# solution = {col: {'possibilities': possibilities,
#                   'cnt_solutions': len(possibilities)} for col, possibilities in solution.items()}


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
    finished_cols = [col for col, pos in sol.items() if len(pos) == 1]
    for finished_col in finished_cols:
        finished_col_name = sol[finished_col][0]
        for col, pos in sol.items():
            if col != finished_col:
                try:
                    pos.remove(finished_col_name)
                except ValueError:
                    pass

    return sol


def check_all_one(sol) -> bool:
    all_one = all([True if len(pos) == 1 else False for pos in sol.values()])

    return all_one


def check_any_zero(sol) -> bool:
    any_zero = any([True if len(pos) == 0 else False for pos in sol.values()])
    return any_zero


def solve(sol):
    if check_all_one(sol):
        print(sol)
        return True

    sol_copy = deepcopy(sol)
    shortest_col = get_shortest_col(sol_copy)
    for field in sol[shortest_col]:
    # field_cnt = Counter(reduce(add, [d['possibilities'] for d in solution.values()]))
    # pick_field_pos()
        sol_copy[shortest_col] = [field]
        sol_copy = strip_possibilities(sol_copy)
        if not check_any_zero(sol_copy):
            if solve(sol_copy):
                return True

        sol[shortest_col].remove(field)

    return False

from copy import deepcopy
solution = remove_possibilities(field_possibilities)
solution_temp = deepcopy(solution)
final_solution = solve(solution)
