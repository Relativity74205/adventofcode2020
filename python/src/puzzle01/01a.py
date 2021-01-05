from puzzle01 import solve, raw_data

target_number = 2020

solution = solve(target_number, map(int, raw_data), 2)
print(f'{solution=}')
