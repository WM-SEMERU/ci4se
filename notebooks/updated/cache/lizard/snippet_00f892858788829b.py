def _get_tiles(board=None, terrain=None, numbers=None):
    if board is not None:
        tiles = _read_tiles_from_string(board)
    else:
        tiles = _generate_tiles(terrain, numbers)
    return tiles