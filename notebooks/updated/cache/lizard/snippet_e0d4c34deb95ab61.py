def ResolveFlats(dem, in_place=False):
    if type(dem) is not rdarray:
        raise Exception('A richdem.rdarray or numpy.ndarray is required!')
    if not in_place:
        dem = dem.copy()
    _AddAnalysis(dem, 'ResolveFlats(dem, in_place={in_place})'.format(
        in_place=in_place))
    demw = dem.wrap()
    _richdem.rdResolveFlatsEpsilon(demw)
    dem.copyFromWrapped(demw)
    if not in_place:
        return dem