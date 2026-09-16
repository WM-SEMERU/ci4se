def pick_flat_z(data):
    zmes = []
    for i in data['zeta']:
        zmes.append(i[:, (0)])
    return np.asarray(zmes)