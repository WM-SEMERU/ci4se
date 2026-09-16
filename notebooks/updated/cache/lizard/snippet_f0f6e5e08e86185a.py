def cube(target, pore_diameter='pore.diameter', throat_area='throat.area'):
    r
    network = target.project.network
    D = target[pore_diameter]
    Tn = network.find_neighbor_throats(pores=target.Ps, flatten=False)
    Tsurf = _np.array([_np.sum(network[throat_area][Ts]) for Ts in Tn])
    value = 6 * D ** 2 - Tsurf
    return value