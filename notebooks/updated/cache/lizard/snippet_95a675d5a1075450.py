def load_parcellation_coords(parcellation_name):
    path = tenetopath[0] + '/data/parcellation/' + parcellation_name + '.csv'
    parc = np.loadtxt(path, skiprows=1, delimiter=',', usecols=[1, 2, 3])
    return parc