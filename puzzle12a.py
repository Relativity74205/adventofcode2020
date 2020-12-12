from pathlib import Path
from dataclasses import dataclass
import math


with open(Path(__file__).parent / "data" / "puzzle12.txt", "r") as f:
    commands = f.read().splitlines()


@dataclass
class Ship:
    x: int
    y: int
    rot: int

    def command(self, full_command: str):
        cmd = full_command[0]
        val = int(full_command[1:])
        if cmd in ('N', 'S', 'E', 'W'):
            self.move(cmd, val)
        elif cmd == 'F':
            self.forward(val)
        elif cmd in ('L', 'R'):
            self.rotate(cmd, val)

    def move(self, cmd: str, val: int):
        if cmd == 'N':
            self.y += val
        elif cmd == 'S':
            self.y -= val
        elif cmd == 'E':
            self.x += val
        elif cmd == 'W':
            self.x -= val

    def forward(self, val: int):
        self.x += math.sin(self.rot * (math.pi / 180)) * val
        self.y += math.cos(self.rot * (math.pi / 180)) * val

    def rotate(self, cmd: str, val: int):
        if cmd == 'R':
            self.rot += val
        elif cmd == 'L':
            self.rot -= val

        self.rot %= 360

    def distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self) -> str:
        return f'Ship(x={self.x}, y={self.y}, rot={self.rot}, dist={self.distance()})'


ship = Ship(0, 0, 90)

for command in commands:
    ship.command(command)
    print(f'{command=}; {ship=}')


print(f'{ship.distance()=}')
