def prior_neighbor(C, alpha=0.001):
    r
    C_sym = C + C.transpose()
    C_sym = C_sym.tocoo()
    data = C_sym.data
    row = C_sym.row
    col = C_sym.col
    data_B = alpha * np.ones_like(data)
    B = coo_matrix((data_B, (row, col)))
    return B