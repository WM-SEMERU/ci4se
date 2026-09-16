def get_atom_map(structure):
    syms = [site.specie.symbol for site in structure]
    unique_pot_atoms = []
    [unique_pot_atoms.append(i) for i in syms if not unique_pot_atoms.count(i)]
    atom_map = {}
    for i, atom in enumerate(unique_pot_atoms):
        atom_map[atom] = i + 1
    return atom_map