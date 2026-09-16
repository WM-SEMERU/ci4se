def perimeter(patch, world_size=(60, 60), neighbor_func=
    get_rook_neighbors_toroidal):
    edge = 0
    patch = set([tuple(i) for i in patch])
    for cell in patch:
        neighbors = neighbor_func(cell, world_size)
        neighbors = [n for n in neighbors if n not in patch]
        edge += len(neighbors)
    return edge