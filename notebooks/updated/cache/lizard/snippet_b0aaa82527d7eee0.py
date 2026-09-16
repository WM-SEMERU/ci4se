def integration(temporalcommunities, staticcommunities):
    if staticcommunities.shape[0] != temporalcommunities.shape[0]:
        raise ValueError(
            'Temporal and static communities have different dimensions')
    alleg = allegiance(temporalcommunities)
    Icoeff = np.zeros(len(staticcommunities))
    for i, statcom in enumerate(len(staticcommunities)):
        Icoeff[i] = np.mean(alleg[i, staticcommunities != statcom])
    return Icoeff