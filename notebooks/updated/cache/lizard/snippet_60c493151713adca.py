def composition(mol):
    mol.require('Valence')
    c = Counter()
    for _, a in mol.atoms_iter():
        c += a.composition()
    return c