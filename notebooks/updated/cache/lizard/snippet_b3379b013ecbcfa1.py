def reorder_brute(p_atoms, q_atoms, p_coord, q_coord):
    unique_atoms = np.unique(p_atoms)
    view_reorder = np.zeros(q_atoms.shape, dtype=int)
    view_reorder -= 1
    for atom in unique_atoms:
        p_atom_idx, = np.where(p_atoms == atom)
        q_atom_idx, = np.where(q_atoms == atom)
        A_coord = p_coord[p_atom_idx]
        B_coord = q_coord[q_atom_idx]
        view = brute_permutation(A_coord, B_coord)
        view_reorder[p_atom_idx] = q_atom_idx[view]
    return view_reorder