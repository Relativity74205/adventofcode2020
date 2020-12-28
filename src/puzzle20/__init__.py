from typing import Dict
from pathlib import Path

import numpy as np


with open(Path(__file__).parent / "puzzle20.txt", "r") as f:
    raw_data = f.read()


def get_tiles(data) -> Dict[int, np.array]:
    tiles = [tile for tile in data.split('\n\n')]
    tiles = [[row for row in tile.split('\n')] for tile in tiles]
    tiles = {int(tile[0].replace('Tile ', '').replace(':', '')): tile[1:] for tile in tiles}
    tiles = {tile_id: np.array([[1 if char == '#' else 0 for char in row] for row in tile])
             for tile_id, tile in tiles.items()}
    return tiles


def get_tile_orientation(tile: np.array) -> Dict[str, np.array]:
    return {'0_no': np.rot90(tile, 0),
            '0_lr': np.fliplr(np.rot90(tile, 0)),
            '0_ud': np.flipud(np.rot90(tile, 0)),
            '1_no': np.rot90(tile, 1),
            '1_lr': np.fliplr(np.rot90(tile, 1)),
            '1_ud': np.flipud(np.rot90(tile, 1)),
            '2_no': np.rot90(tile, 2),
            '2_lr': np.fliplr(np.rot90(tile, 2)),
            '2_ud': np.flipud(np.rot90(tile, 2)),
            '3_no': np.rot90(tile, 3),
            '3_lr': np.fliplr(np.rot90(tile, 3)),
            '3_ud': np.flipud(np.rot90(tile, 3)),
            }


def get_tiles_orientations(tiles: Dict[int, np.array]) -> Dict[int, Dict[str, np.array]]:
    tiles_possibilities = {tile_id: get_tile_orientation(tile) for tile_id, tile in tiles.items()}

    return tiles_possibilities
