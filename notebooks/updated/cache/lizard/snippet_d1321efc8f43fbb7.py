def initialise_arrays(group, f):
    for node in ['pos_x', 'pos_y', 'pos_z', 'dir_x', 'dir_y', 'dir_z', 'du',
        'floor', 't0']:
        if node in ['floor', 'du']:
            atom = U1_ATOM
        else:
            atom = F4_ATOM
        f.create_earray(group, node, atom, (0,), filters=FILTERS)