def or_constraint(v=0, sense='maximize'):
    assert v in [0, 1], 'v must be 0 or 1 instead of %s' % v.__repr__()
    model, x, y, z = _init()
    r = model.addVar('r', 'B')
    model.addConsOr([x, y, z], r)
    model.addCons(x == v)
    model.setObjective(r, sense=sense)
    _optimize('OR', model)