def largest_graph(mol):
    mol.require('Valence')
    mol.require('Topology')
    m = clone(mol)
    if m.isolated:
        for k in itertools.chain.from_iterable(m.isolated):
            m.remove_atom(k)
    return m