def vclose(L, V):
    lam, X = 0, []
    for k in range(3):
        lam = lam + V[k] * L[k]
    beta = np.sqrt(1.0 - lam ** 2)
    for k in range(3):
        X.append(old_div(V[k] - lam * L[k], beta))
    return X