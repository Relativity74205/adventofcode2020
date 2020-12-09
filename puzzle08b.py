from pathlib import Path

with open(Path(__file__).parent / "data" / "puzzle08.txt", "r") as f:
    raw_data = f.read().splitlines()


combinations = [raw_data]
for i in range(len(raw_data)):
    modified_data = raw_data.copy()
    cmd = modified_data[i].split(' ')[0]
    num = modified_data[i].split(' ')[1]
    if cmd == 'jmp':
        modified_data[i] = f'nop {num}'
    elif cmd == 'nop':
        modified_data[i] = f'jmp {num}'
    elif cmd == 'acc':
        continue

    combinations.append(modified_data)


for combination in combinations:
    i = 0
    acc = 0
    visited = set()
    while True:
        visited.add(i)
        print(f'{i=} {combination[i]}')
        cmd = combination[i].split(' ')[0]
        num = combination[i].split(' ')[1]
        if cmd == 'acc':
            acc += int(num)
            i += 1
        elif cmd == 'jmp':
            i += int(num)
        elif cmd == 'nop':
            i += 1

        if i in visited:
            print(f'Infinite loop: {acc=}')
            break

        if i >= len(combination):
            print(f'Program finished: {acc=}')
            import sys
            sys.exit(0)
