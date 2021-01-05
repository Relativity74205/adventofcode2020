from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent / "data" / "puzzle10.txt", "r") as f:
    raw_data = f.read().splitlines()

# the following four lines are awful...
data = [0] + sorted(list(map(int, raw_data)))
deltas = [data[i + 1] - data[i] for i in range(len(data) - 1)]
divider_indices = [0] + [i + 1 for i, delta in enumerate(deltas) if delta == 3] + [len(data)]
sub_networks = [data[divider_indices[i]: divider_indices[i + 1]] for i in range(len(divider_indices) - 1)]


def process_sub_network(sub_net):
    max_index = len(sub_net) - 1
    to_visit = [0]
    paths = 0

    while len(to_visit) > 0:
        current_index = to_visit.pop()
        if current_index == max_index:
            paths += 1
            continue

        for i in range(1, min(max_index - current_index, 3) + 1):
            to_visit.append(current_index + i)

    return paths


amount_paths = 1
for sub_network in sub_networks:
    amount_paths *= process_sub_network(sub_network)

print(f'{amount_paths=}')
