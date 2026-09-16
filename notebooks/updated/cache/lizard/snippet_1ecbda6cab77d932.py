def _create_structure_array(structure_array, voxelspacing):
    try:
        structure_array = [(s / float(vs)) for s, vs in zip(structure_array,
            voxelspacing)]
    except TypeError:
        structure_array = [(structure_array / float(vs)) for vs in voxelspacing
            ]
    return structure_array