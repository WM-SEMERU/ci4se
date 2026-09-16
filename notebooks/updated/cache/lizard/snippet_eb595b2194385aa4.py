def from_indigo(idgmol, assign_descriptor=True):
    mol = Compound()
    for atom in idgmol.iterateAtoms():
        key = atom.index()
        a = Atom(atom.symbol())
        a.coords = list(atom.xyz())
        mol.add_atom(key, a)
    for bond in idgmol.iterateBonds():
        u = bond.source()
        v = bond.destination()
        b = Bond()
        b.order = int(bond.bondOrder())
        mol.add_bond(u.index(), v.index(), b)
    if assign_descriptor:
        molutil.assign_descriptors(mol)
    return mol