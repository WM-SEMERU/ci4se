def n_bifurcation_points(neurites, neurite_type=NeuriteType.all):
    return n_sections(neurites, neurite_type=neurite_type, iterator_type=
        Tree.ibifurcation_point)