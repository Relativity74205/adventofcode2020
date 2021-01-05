from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle25.txt", "r") as f:
    raw_data = f.read().splitlines()

public_key_card = int(raw_data[0])
public_key_door = int(raw_data[1])


def calc_loop_size(public_key):
    val = 1
    loop = 0
    while True:
        loop += 1
        val = (val * 7) % 20201227
        if val == public_key:
            return loop


def calc_encryption_key(subject_number, loop_size):
    n = 1
    for i in range(loop_size):
        n = (n * subject_number) % 20201227
    return n


loop_size = calc_loop_size(public_key_card)
enc_key = calc_encryption_key(public_key_door, loop_size)
print(enc_key)
