def _create_node_matrix_from_coord_section(specs):
    distances = specs['NODE_COORD_SECTION']
    specs['MATRIX'] = {}
    for i in distances:
        origin = tuple(distances[i])
        specs['MATRIX'][i] = {}
        for j in specs['NODE_COORD_SECTION']:
            destination = tuple(distances[j])
            distance = calculate_euc_distance(origin, destination)
            specs['MATRIX'][i][j] = distance