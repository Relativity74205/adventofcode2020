from puzzle01 import solve, data

target_number = 2020

solution = solve(target_number, map(int, data), 3)
print(f'{solution=}')
