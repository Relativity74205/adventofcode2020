from collections import defaultdict

start_numbers = [8, 13, 1, 0, 18, 9]
end_round = 30_000_000
numbers_spoken = defaultdict(list)

for i, start_number in enumerate(start_numbers, start=1):
    numbers_spoken[start_number].append(i)

current_numbers = start_numbers.copy()
for current_round in range(len(numbers_spoken) + 1, end_round + 1):
    last_number = current_numbers[-1]
    if len(numbers_spoken[last_number]) == 1:
        current_number = 0
    else:
        current_number = numbers_spoken[last_number][-1] - numbers_spoken[last_number][-2]

    current_numbers.append(current_number)
    numbers_spoken[current_number].append(current_round)
