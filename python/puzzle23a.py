import time
from typing import List
from collections import deque


input_list = '193467258'
# moves = 10_000_000
moves = 100
max_target_label = 9


def get_destination_cup(arr: deque, pick_up_values: List, target_label: int) -> int:
    while True:
        target_label -= 1
        if target_label <= 0:
            target_label = max_target_label
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


def get_result(arr: deque) -> str:
    pos_one = arr.index(1)
    return ''.join([str(arr[(pos_one + 1 + i) % 9]) for i in range(8)])


arr_start = deque(map(int, input_list))
arr_output = arr_start.copy()

t1 = time.time()
for _ in range(moves):
    arr_output = calc_move(arr_output)
t2 = time.time()

print(t2-t1)
print(f'{get_result(arr_output)=}')
#  25468379
