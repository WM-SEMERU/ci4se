def windyields(self, ini, end, delta, **keyw):
    if ('tmass' in keyw) == False:
        keyw['tmass'] = 'mass'
    if ('abund' in keyw) == False:
        keyw['abund'] = 'iso_massf'
    if ('cycle' in keyw) == False:
        keyw['cycle'] = 'cycle'
    print('Windyields() initialised.  Reading files...')
    ypsinit = []
    niso = 0
    X_i = []
    E_i = []
    totalmass = []
    ypssurf = []
    cycles = []
    first = True
    wc = self._windcalc
    cycleret = self.se.cycles
    retrieve = self.se.get
    capp = cycles.extend
    tapp = totalmass.extend
    yapp = ypssurf.extend
    for i in range(ini, end + 1, delta):
        step = int(i)
        capp([int(cycleret[i - ini])])
        tapp([retrieve(step, keyw['tmass'])])
        yapp([retrieve(step, keyw['abund'])])
    print('Reading complete.  Calculating yields and ejected masses...')
    nsteps = len(cycles) - 1
    niso = len(ypssurf[0])
    X_i = np.zeros([niso], float)
    E_i = np.zeros([niso], float)
    X_i, E_i = wc(first, totalmass, nsteps, niso, ypssurf, ypsinit, X_i,
        E_i, cycles)
    return X_i, E_i