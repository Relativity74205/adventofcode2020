from typing import Dict, List, Tuple
from pathlib import Path

import numpy as np


TILE_WIDTH = 10
with open(Path(__file__).parent / "puzzle20.txt", "r") as f:
    raw_data = f.read()


def get_tiles(data) -> Dict[int, np.array]:
    tiles = [tile for tile in data.split('\n\n')]
    tiles = [[row for row in tile.split('\n')] for tile in tiles]
    tiles = {int(tile[0].replace('Tile ', '').replace(':', '')): tile[1:] for tile in tiles}
    tiles = {tile_id: np.array([[1 if char == '#' else 0 for char in row] for row in tile])
             for tile_id, tile in tiles.items()}
    return tiles


def get_tile_orientation(tile: np.array) -> List[np.array]:
    return [np.rot90(tile, 0),
            np.flipud(np.rot90(tile, 0)),
            np.rot90(tile, 1),
            np.flipud(np.rot90(tile, 1)),
            np.rot90(tile, 2),
            np.flipud(np.rot90(tile, 2)),
            np.rot90(tile, 3),
            np.flipud(np.rot90(tile, 3)),
            ]


def get_tiles_orientations(tiles: Dict[int, np.array]) -> Dict[int, List[np.array]]:
    tiles_possibilities = {tile_id: get_tile_orientation(tile) for tile_id, tile in tiles.items()}

    return tiles_possibilities


def get_full_slice(x: int, y: int):
    return tuple([slice(x * TILE_WIDTH, (x + 1) * TILE_WIDTH), slice(y * TILE_WIDTH, (y + 1) * TILE_WIDTH), ])


def get_empty_neighbors(added_tiles: List[Tuple[int, int]], x: int, y: int):
    empty_neighbors = []
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if (x + dx, y + dy) not in added_tiles:
            empty_neighbors.append((dx, dy))
    return empty_neighbors


def set_start_tile(arr: np.array, arr_id: np.array, added_tiles: List[Tuple[int, int]], start_tile: np.array,
                   start_coords: Tuple[int, int]):
    arr_id[slice(*start_coords)] = start_tile[0]
    arr[get_full_slice(*start_coords)] = start_tile[1][0]
    added_tiles.append(start_coords)

    return arr, arr_id, added_tiles


def compare_tiles(old_tile: np.array, new_tile: np.array, empty_neighbors: List[Tuple[int, int]]):
    for empty_neighbor in empty_neighbors:
        if empty_neighbor == (0, 1) and np.all(old_tile[:, -1] == new_tile[:, 0]):
            return empty_neighbor
        elif empty_neighbor == (0, -1) and np.all(old_tile[:, 0] == new_tile[:, -1]):
            return empty_neighbor
        elif empty_neighbor == (1, 0) and np.all(old_tile[-1, :] == new_tile[0, :]):
            return empty_neighbor
        elif empty_neighbor == (-1, 0) and np.all(old_tile[0, :] == new_tile[-1, :]):
            return empty_neighbor

    return None


def search_next_fit(arr: np.array, arr_id: np.array, added_tiles: List[Tuple[int, int]], tiles_possibilities: Dict):
    for tile_id, tile_possibilities in tiles_possibilities.items():
        for tile in tile_possibilities:
            for tile_x, tile_y in added_tiles:
                empty_neighbors = get_empty_neighbors(added_tiles, tile_x, tile_y)
                match_tile = compare_tiles(arr[get_full_slice(tile_x, tile_y)], tile, empty_neighbors)
                if match_tile:
                    x = tile_x + match_tile[0]
                    y = tile_y + match_tile[1]
                    added_tiles.append((x, y))
                    arr_id[x, y] = tile_id
                    arr[get_full_slice(x, y)] = tile
                    return arr, arr_id, added_tiles, tile_id
    return arr, arr_id, added_tiles, None


def clean_arr(arr: np.array) -> np.array:
    non_zero_entries = np.argwhere(arr > 0)
    x_min = min(non_zero_entries[:, 0])
    x_max = max(non_zero_entries[:, 0])
    y_min = min(non_zero_entries[:, 1])
    y_max = max(non_zero_entries[:, 1])

    return arr[slice(x_min, x_max + 1), slice(y_min, y_max + 1)]


def create_arrays(data):
    tiles = get_tiles(data)
    tiles_possibilities = get_tiles_orientations(tiles)
    edge_length = int(np.sqrt(len(tiles)))
    arr_ids = np.zeros((3 * edge_length, 3 * edge_length), dtype=np.int32)
    arr_pixels = np.zeros((3 * edge_length * TILE_WIDTH, 3 * edge_length * TILE_WIDTH), dtype=np.int8)
    finished_tiles = []

    start_tile = tiles_possibilities.popitem()
    x = y = int(1.5 * edge_length)
    arr_pixels, arr_ids, finished_tiles = set_start_tile(arr_pixels, arr_ids, finished_tiles, start_tile, (x, y, ))
    while tiles_possibilities:
        arr_pixels, arr_ids, finished_tiles, next_tile_id = search_next_fit(arr_pixels,
                                                                            arr_ids,
                                                                            finished_tiles,
                                                                            tiles_possibilities)
        if next_tile_id:
            tiles_possibilities.pop(next_tile_id)

    arr_ids = clean_arr(arr_ids)
    arr_pixels = clean_arr(arr_pixels)

    return arr_ids, arr_pixels
