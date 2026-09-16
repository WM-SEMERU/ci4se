def equal(mol, query, largest_only=True, ignore_hydrogen=True):
    m = molutil.clone(mol)
    q = molutil.clone(query)
    if largest_only:
        m = molutil.largest_graph(m)
        q = molutil.largest_graph(q)
    if ignore_hydrogen:
        m = molutil.make_Hs_implicit(m)
        q = molutil.make_Hs_implicit(q)
    if molutil.mw(m) == molutil.mw(q):
        gm = GraphMatcher(q.graph, m.graph, node_match=atom_match)
        return gm.is_isomorphic()
    return False