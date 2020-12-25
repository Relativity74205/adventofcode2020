from collections import deque
import time
from typing import List


input_list = '193467258'
# input_list = '389125467'
moves = 100
# moves = 10_000_000
amount_labels = 1_000_000


class Circle:
    def __init__(self, cups: List):
        self.circle = {}
        for cup1, cup2 in zip(cups, cups[1:] + cups[0]):
            self.circle[cup1] = cup2


def get_destination_cup(arr: deque, pick_up_values: List, target_label: int) -> int:
    while True:
        target_label -= 1
        if target_label <= 0:
            target_label = amount_labels
        if target_label not in pick_up_values:
            return arr.index(target_label)


def calc_move(arr: deque) -> deque:
    current_cup_value = arr[0]
    arr.rotate(-1)
    pick_up_values = [arr.popleft() for _ in range(3)]
    destination_cup_index = get_destination_cup(arr, pick_up_values, current_cup_value)
    arr.rotate(- destination_cup_index - 1)
    arr.appendleft(pick_up_values[2])
    arr.appendleft(pick_up_values[1])
    arr.appendleft(pick_up_values[0])
    arr.rotate(-(- destination_cup_index - 1))

    return arr


# def get_result(arr: deque) -> str:
#     pos_one = arr.index(1)
#     return ''.join([str(arr[(pos_one + 1 + i) % 9]) for i in range(8)])


arr_start = deque(list(map(int, input_list)) + list(range(10, amount_labels + 1)))
arr_output = arr_start.copy()


def solve(arr: deque) -> deque:
    for i in range(moves):
        print(f'move {i=}')
        arr = calc_move(arr)

    return arr


# arr_output = solve(arr_output)


# print(f'{get_result(arr_output)=}')
#  25468379
import cProfile
cProfile.run('solve(arr_output)')
