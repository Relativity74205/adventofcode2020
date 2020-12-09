from pathlib import Path

with open(Path(__file__).parent / "data" / "puzzle02.txt", "r") as f:
    data = f.read().splitlines()

amount_valid_passwords = 0

for password_entry in data:
    policy = password_entry.split(':')[0]
    password = password_entry.split(':')[1].strip()
    first_occurrence = int(policy.split(' ')[0].split('-')[0]) - 1
    second_occurrence = int(policy.split(' ')[0].split('-')[1]) - 1
    policy_char = policy.split(' ')[1]

    if (password[first_occurrence] == policy_char) != (password[second_occurrence] == policy_char):
        amount_valid_passwords += 1

print(f'{amount_valid_passwords=}')
