def gaussianize(Y):
    N, P = Y.shape
    YY = toRanks(Y)
    quantiles = (sp.arange(N) + 0.5) / N
    gauss = st.norm.isf(quantiles)
    Y_gauss = sp.zeros((N, P))
    for i in range(P):
        Y_gauss[:, (i)] = gauss[YY[:, (i)]]
    Y_gauss *= -1
    return Y_gauss