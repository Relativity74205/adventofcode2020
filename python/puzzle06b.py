from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle06.txt", "r") as f:
    data = f.read().splitlines()

groups = [[]]
counter = 0
for row in data:
    if row == '':
        counter += 1
        groups.append([])
        continue

    groups[counter].append(row)

answered_group_questions = 0
for group in groups:
    s = set(group[0])
    for people in group[1:]:
        s = s.intersection(set(people))

    answered_group_questions += len(s)

print(f'{answered_group_questions=}')
