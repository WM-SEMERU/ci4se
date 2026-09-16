def get_bond_symmetry(site_symmetry, lattice, positions, atom_center,
    atom_disp, symprec=1e-05):
    bond_sym = []
    pos = positions
    for rot in site_symmetry:
        rot_pos = np.dot(pos[atom_disp] - pos[atom_center], rot.T) + pos[
            atom_center]
        diff = pos[atom_disp] - rot_pos
        diff -= np.rint(diff)
        dist = np.linalg.norm(np.dot(lattice, diff))
        if dist < symprec:
            bond_sym.append(rot)
    return np.array(bond_sym)