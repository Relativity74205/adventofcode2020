from pathlib import Path
from dataclasses import dataclass
import math


with open(Path(__file__).parent / "data" / "puzzle12.txt", "r") as f:
    commands = f.read().splitlines()


@dataclass
class Ship:
    x: int
    y: int
    way_x: int
    way_y: int

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
            self.way_y += val
        elif cmd == 'S':
            self.way_y -= val
        elif cmd == 'E':
            self.way_x += val
        elif cmd == 'W':
            self.way_x -= val

    def forward(self, val: int):
        # self.x += math.sin(self.rot * (math.pi / 180)) * int(cmd[1:])
        # self.y += math.cos(self.rot * (math.pi / 180)) * int(cmd[1:])
        self.x += self.way_x * val
        self.y += self.way_y * val

    def rotate(self, cmd: str, val: int):
        if cmd == 'R':
            val *= -1

        way_rot = math.atan2(self.way_y, self.way_x) + val * (math.pi / 180)
        dist = math.sqrt(self.way_x**2 + self.way_y**2)

        self.way_x = int(round(math.cos(way_rot) * dist, 0))
        self.way_y = int(round(math.sin(way_rot) * dist, 0))

    def distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self) -> str:
        return f'Ship(x={self.x}, y={self.y}, way_x={self.way_x}, way_y={self.way_y}, dist={self.distance()})'


ship = Ship(0, 0, 10, 1)

for command in commands:
    ship.command(command)

    print(f'{command=}; {ship=}')


print(f'{ship.distance()=}')
