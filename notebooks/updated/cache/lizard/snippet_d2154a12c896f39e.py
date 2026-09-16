def nearest_tile_to_node_using_tiles(tile_ids, node_coord):
    for tile_id in tile_ids:
        if node_coord - tile_id_to_coord(tile_id) in _tile_node_offsets.keys():
            return tile_id
    logging.critical('Did not find a tile touching node={}'.format(node_coord))