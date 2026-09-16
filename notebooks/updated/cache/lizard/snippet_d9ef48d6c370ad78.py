def _exprcomp(node):
    try:
        comp = _LITS[node.data()]
    except KeyError:
        comp = _LITS[node.data()] = Complement(node)
    return comp