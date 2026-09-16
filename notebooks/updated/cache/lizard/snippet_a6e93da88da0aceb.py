def tile_id_in_direction(from_tile_id, direction):
    coord_from = tile_id_to_coord(from_tile_id)
    for offset, dirn in _tile_tile_offsets.items():
        if dirn == direction:
            coord_to = coord_from + offset
            if coord_to in legal_tile_coords():
                return tile_id_from_coord(coord_to)
    return None