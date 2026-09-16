def hitting_probability(P, target):
    if hasattr(target, '__len__'):
        target = np.array(target)
    else:
        target = np.array([target])
    n = np.shape(P)[0]
    nontarget = np.array(list(set(range(n)) - set(target)), dtype=int)
    stable = np.where(np.isclose(np.diag(P), 1) == True)[0]
    origin = np.array(list(set(nontarget) - set(stable)), dtype=int)
    A = P[(origin), :][:, (origin)] - np.eye(len(origin))
    b = np.sum(-P[(origin), :][:, (target)], axis=1)
    x = np.linalg.solve(A, b)
    xfull = np.ones(n)
    xfull[origin] = x
    xfull[target] = 1
    xfull[stable] = 0
    return xfull