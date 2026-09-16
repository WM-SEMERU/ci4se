def rho_hv(scatterer):
    Z = scatterer.get_Z()
    a = (Z[2, 2] + Z[3, 3]) ** 2 + (Z[3, 2] - Z[2, 3]) ** 2
    b = Z[0, 0] - Z[0, 1] - Z[1, 0] + Z[1, 1]
    c = Z[0, 0] + Z[0, 1] + Z[1, 0] + Z[1, 1]
    return np.sqrt(a / (b * c))