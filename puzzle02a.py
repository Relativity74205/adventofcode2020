from pathlib import Path
from collections import Counter

with open(Path(__file__).parent / "data" / "puzzle02.txt", "r") as f:
    data = f.read().splitlines()

amount_valid_passwords = 0

for password_entry in data:
    policy = password_entry.split(':')[0]
    password = password_entry.split(':')[1].strip()
    policy_char_lower_amount = int(policy.split(' ')[0].split('-')[0])
    policy_char_upper_amount = int(policy.split(' ')[0].split('-')[1])
    policy_char = policy.split(' ')[1]

    password_char_counts = Counter(password)
    policy_char_count = password_char_counts[policy_char]
    if policy_char_lower_amount <= policy_char_count <= policy_char_upper_amount:
        amount_valid_passwords += 1

print(f'{amount_valid_passwords=}')
