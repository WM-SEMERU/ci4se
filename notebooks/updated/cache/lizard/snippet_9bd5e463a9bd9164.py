def merge_systems(sysa, sysb, bounding=0.2):
    if bounding is not False:
        if sysa.box_vectors is not None:
            periodicity = sysa.box_vectors.diagonal()
        else:
            periodicity = False
        p = overlapping_points(sysb.r_array, sysa.r_array, cutoff=bounding,
            periodic=periodicity)
        sel = np.ones(len(sysa.r_array), dtype=np.bool)
        sel[p] = False
        sysa = subsystem_from_atoms(sysa, sel)
    sysres = System.empty(sysa.n_mol + sysb.n_mol, sysa.n_atoms + sysb.n_atoms)
    for attr in type(sysa).attributes:
        attr.assign(sysres, attr.concatenate(sysa, sysb))
    offset = sysa.mol_indices[-1] + sysa.mol_n_atoms[-1]
    sysres.mol_indices[0:sysa.n_mol] = sysa.mol_indices.copy()
    sysres.mol_indices[sysa.n_mol:] = sysb.mol_indices.copy() + offset
    sysres.mol_n_atoms = np.concatenate([sysa.mol_n_atoms, sysb.mol_n_atoms])
    sysres.box_vectors = sysa.box_vectors
    return sysres