from pathlib import Path
from collections import deque


with open(Path(__file__).parent / "data" / "puzzle22.txt", "r") as f:
    raw_data = f.read()


def populate_deque(data) -> deque:
    p = deque()
    rows = data.split('\n')
    for row in rows[1:]:
        if row != '':
            p.append(int(row))

    return p


player1 = populate_deque(raw_data.split('\n\n')[0])
player2 = populate_deque(raw_data.split('\n\n')[1])


def play_game(p1: deque, p2: deque) -> (deque, deque):
    p1, p2 = p1.copy(), p2.copy()
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.append(c1), p1.append(c2)
        else:
            p2.append(c2), p2.append(c1)

    return p1, p2


def get_score(p1: deque, p2: deque) -> int:
    winner_deque = p1 if len(p1) > 0 else p2
    score = sum([a * b for a, b in zip(reversed(list(winner_deque)), range(1, len(winner_deque) + 1))])

    return score


player1_end, player2_end = play_game(player1, player2)
game_score = get_score(player1_end, player2_end)
print(f'{game_score=}')
