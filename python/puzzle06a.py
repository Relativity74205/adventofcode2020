from pathlib import Path

with open(Path(__file__).parent / "data" / "puzzle06.txt", "r") as f:
    data = f.read().replace('\n\n', '_').replace('\n', '').replace('_', '\n').splitlines()

answered_group_questions = 0
for group in data:
    answered_group_questions += len(set(group))

print(f'{answered_group_questions=}')
