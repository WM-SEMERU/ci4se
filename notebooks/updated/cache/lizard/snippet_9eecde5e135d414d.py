def center_of_mass(entity, geometric=False):
    if isinstance(entity, Entity.Entity):
        atom_list = entity.get_atoms()
    elif hasattr(entity, '__iter__') and [x for x in entity if x.level == 'R']:
        atom_list = []
        for res in entity:
            atom_list.extend(list(res.get_atoms()))
    elif hasattr(entity, '__iter__') and [x for x in entity if x.level == 'A']:
        atom_list = entity
    else:
        raise ValueError(
            """Center of Mass can only be calculated from the following objects:
Structure, Model, Chain, Residue, list of Atoms."""
            )
    masses = []
    positions = [[], [], []]
    for atom in atom_list:
        masses.append(atom.mass)
        for i, coord in enumerate(np.array(atom.coord).tolist()):
            positions[i].append(coord)
    if 'ukn' in set(masses) and not geometric:
        raise ValueError(
            """Some Atoms don't have an element assigned.
Try adding them manually or calculate the geometrical center of mass instead."""
            )
    if geometric:
        return [(sum(coord_list) / len(masses)) for coord_list in positions]
    else:
        w_pos = [[], [], []]
        for atom_index, atom_mass in enumerate(masses):
            w_pos[0].append(positions[0][atom_index] * atom_mass)
            w_pos[1].append(positions[1][atom_index] * atom_mass)
            w_pos[2].append(positions[2][atom_index] * atom_mass)
        return [(sum(coord_list) / sum(masses)) for coord_list in w_pos]