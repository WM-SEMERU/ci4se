def mctransp(I, J, K, c, d, M):
    model = Model('multi-commodity transportation')
    x = {}
    for i, j, k in c:
        x[i, j, k] = model.addVar(vtype='C', name='x(%s,%s,%s)' % (i, j, k))
    for i in I:
        for k in K:
            model.addCons(sum(x[i, j, k] for j in J if (i, j, k) in x) == d
                [i, k], 'Demand(%s,%s)' % (i, k))
    for j in J:
        model.addCons(sum(x[i, j, k] for i, j2, k in x if j2 == j) <= M[j],
            'Capacity(%s)' % j)
    model.setObjective(quicksum(c[i, j, k] * x[i, j, k] for i, j, k in x),
        'minimize')
    model.data = x
    return model