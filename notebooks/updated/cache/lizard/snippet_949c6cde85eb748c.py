def kcover(I, J, c, k):
    model = Model('k-center')
    z, y, x = {}, {}, {}
    for i in I:
        z[i] = model.addVar(vtype='B', name='z(%s)' % i, obj=1)
    for j in J:
        y[j] = model.addVar(vtype='B', name='y(%s)' % j)
        for i in I:
            x[i, j] = model.addVar(vtype='B', name='x(%s,%s)' % (i, j))
    for i in I:
        model.addCons(quicksum(x[i, j] for j in J) + z[i] == 1, 
            'Assign(%s)' % i)
        for j in J:
            model.addCons(x[i, j] <= y[j], 'Strong(%s,%s)' % (i, j))
    model.addCons(sum(y[j] for j in J) == k, 'k_center')
    model.data = x, y, z
    return model