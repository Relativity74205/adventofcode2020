from typing import List


input_list = '193467258'
moves = 10_000_000
amount_labels = 1_000_000


class Circle:
    def __init__(self, cups: List):
        self.circle = {}
        self.current_cup = cups[0]
        for cup1, cup2 in zip(cups, cups[1:] + [cups[0]]):
            self.circle[cup1] = cup2

    def pop_next_cups(self, cup: int, times: int) -> List[int]:
        cups = []
        for _ in range(times):
            next_cup = self.circle[cup]
            cups.append(next_cup)
            next_next_cup = self.circle.pop(next_cup)
            self.circle[cup] = next_next_cup

        return cups

    def insert_cups(self, cup: int, vals: List[int]):
        for val in reversed(vals):
            self.circle[cup], self.circle[val] = val, self.circle[cup]

    # def __repr__(self):
    #     s = ''
    #     current_cup = 1
    #     for _ in range(len(self.circle) - 1):
    #         s += str(self.circle[current_cup])
    #         current_cup = self.circle[current_cup]
    #
    #     return s
    def __repr__(self):
        next_cup = self.circle[1]
        next_next_cup = self.circle[next_cup]

        return f'{next_cup=}, {next_next_cup=}, prod:{next_cup*next_next_cup}'


def get_destination_cup(current_cup: int, pick_up_values: List) -> int:
    target_label = current_cup
    while True:
        target_label -= 1
        if target_label <= 0:
            target_label = amount_labels
        if target_label not in pick_up_values:
            return target_label


def calc_move(cups: Circle) -> Circle:
    pick_up_values = cups.pop_next_cups(cups.current_cup, 3)
    destination_cup = get_destination_cup(cups.current_cup, pick_up_values)
    cups.insert_cups(destination_cup, pick_up_values)
    cups.current_cup = cups.circle[cups.current_cup]

    return cups


def solve(cups: Circle) -> Circle:
    for i in range(moves):
        cups = calc_move(cups)

    return cups


cups_list = list(map(int, input_list)) + list(range(10, amount_labels + 1))
cups_circle = Circle(cups_list)
cups_circle = solve(cups_circle)
print(cups_circle)
