def apply_gravity(repulsion, nodes, gravity, scaling_ratio):
    for i in range(0, len(nodes)):
        repulsion.apply_gravitation(nodes[i], gravity / scaling_ratio)