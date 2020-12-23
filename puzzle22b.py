from pathlib import Path
from collections import deque
import logging


with open(Path(__file__).parent / "data" / "puzzle22.txt", "r") as f:
    raw_data = f.read()


logging.basicConfig(level=logging.INFO, format='%(module)s %(levelname)s %(asctime)s %(message)s')
logger = logging.getLogger(__name__)


def populate_deque(data) -> deque:
    p = deque()
    rows = data.split('\n')
    for row in rows[1:]:
        if row != '':
            p.append(int(row))

    return p


player1 = populate_deque(raw_data.split('\n\n')[0])
player2 = populate_deque(raw_data.split('\n\n')[1])
game_number = 1


def play_game(p1_input: deque, p2_input: deque, game: int) -> (deque, deque):
    logger.info(f'Starting game number {game}.')
    p1, p2 = p1_input.copy(), p2_input.copy()
    p1_decks = set()
    p2_decks = set()
    game_round = 1
    while p1 and p2:
        logger.info(f'Playing round {game_round} of game {game}.')
        if tuple(p1) in p1_decks and tuple(p2) in p2_decks:
            return p1, deque()
        else:
            p1_decks.add(tuple(p1)), p2_decks.add(tuple(p2))

        c1, c2 = p1.popleft(), p2.popleft()
        if c1 <= len(p1) and c2 <= len(p2):
            global game_number
            game_number += 1
            p1_sub, p2_sub = play_game(deque(list(p1)[:c1]), deque(list(p2)[:c2]), game_number)
            if p1_sub:
                p1.append(c1), p1.append(c2)
            elif p2_sub:
                p2.append(c2), p2.append(c1)
            else:
                raise RuntimeError('gnargh')
        else:
            if c1 > c2:
                p1.append(c1), p1.append(c2)
            else:
                p2.append(c2), p2.append(c1)
        game_round += 1

    return p1, p2


def get_score(p1: deque, p2: deque) -> int:
    winner_deque = p1 if len(p1) > 0 else p2
    score = sum([a * b for a, b in zip(reversed(list(winner_deque)), range(1, len(winner_deque) + 1))])

    return score


player1_end, player2_end = play_game(player1, player2, 1)
game_score = get_score(player1_end, player2_end)
print(f'{game_score=}')
