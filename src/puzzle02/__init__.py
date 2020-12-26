from pathlib import Path

with open(Path(__file__).parent / "puzzle02.txt", "r") as f:
    raw_data = f.read().splitlines()
