from pathlib import Path
from typing import Iterator


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


def check_field(value: int) -> int:
    for value_range in ranges.values():
        if (value_range['min1'] <= value <= value_range['max1']
                or value_range['min2'] <= value <= value_range['max2']):
            return 0
    return value


def valid_ticket(values: Iterator[int]) -> int:
    fields = [check_field(value) for value in values]

    return sum(fields)


valid_tickets = [valid_ticket(map(int, ticket.split(','))) for ticket in nearby_ticket_data]

print(f'{sum(valid_tickets)=}')
