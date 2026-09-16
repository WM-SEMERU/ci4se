def nb_ll(data, P, R):
    genes, cells = data.shape
    clusters = P.shape[1]
    lls = np.zeros((cells, clusters))
    for c in range(clusters):
        P_c = P[:, (c)].reshape((genes, 1))
        R_c = R[:, (c)].reshape((genes, 1))
        ll = gammaln(R_c + data) - gammaln(R_c)
        ll += data * np.log(P_c) + xlog1py(R_c, -P_c)
        lls[:, (c)] = ll.sum(0)
    return lls