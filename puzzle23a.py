import typing as ty


input_list = '193467258'
moves = 100


def get_destination_cup(arr: ty.List, target_label: int) -> int:
    while True:
        if target_label in arr:
            return arr.index(target_label)
        else:
            target_label -= 1
            if target_label <= 0:
                target_label = 9


def move_circle(arr: ty.List, times: int) -> ty.List:
    if times > 0:
        for _ in range(times):
            arr.append(arr[0])
            arr.remove(arr[0])
    elif times < 0:
        for _ in range(times):
            arr.insert(0, arr[-1])
            arr.remove(arr[-1])

    return arr


arr = list(map(int, input_list))
current_cup_index = 0
for _ in range(moves):
    # print(f'{current_cup_index=}')
    current_cup_value = arr[current_cup_index % 9]
    pick_up_indices = [ele % 9 for ele in range(current_cup_index + 1, current_cup_index + 4)]
    pick_up_values = [ele for i, ele in enumerate(arr) if i in pick_up_indices]
    temp_arr = [ele for i, ele in enumerate(arr) if i not in pick_up_indices]
    destination_cup_index = get_destination_cup(temp_arr, arr[current_cup_index] - 1)
    destination_cup_value = temp_arr[destination_cup_index]
    for i, pick_up_index in enumerate(pick_up_indices):
        temp_arr.insert(destination_cup_index + i + 1, arr[pick_up_index])
    new_current_cup_index = temp_arr.index(current_cup_value)
    # temp_arr = move_circle(temp_arr, new_current_cup_index - current_cup_index)
    arr = temp_arr.copy()
    current_cup_index = new_current_cup_index + 1
    current_cup_index = current_cup_index % 9


def get_result(arr: ty.List) -> str:
    pos_one = arr.index(1)
    return ''.join([str(arr[(pos_one + 1 + i) % 9]) for i in range(8)])


print(f'{get_result(arr)=}')
#  25468379
