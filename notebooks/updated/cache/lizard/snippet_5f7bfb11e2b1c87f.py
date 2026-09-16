def _get_assumptions(t):
    if t.op in ('__le__', '__lt__', 'ULE', 'ULT'):
        return [t.args[0] >= 0]
    elif t.op in ('__ge__', '__gt__', 'UGE', 'UGT'):
        return [t.args[0] <= 2 ** len(t.args[0]) - 1]
    elif t.op in ('SLE', 'SLT'):
        return [_all_operations.SGE(t.args[0], -(1 << len(t.args[0]) - 1))]
    elif t.op in ('SGE', 'SGT'):
        return [_all_operations.SLE(t.args[0], (1 << len(t.args[0]) - 1) - 1)]
    else:
        return []