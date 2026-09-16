def mzminus(df, minus=0, noise=10000):
    mol_ions = ((df.values > noise) * df.columns).max(axis=1) - minus
    mol_ions[np.abs(mol_ions) < 0] = 0
    d = np.abs(np.ones(df.shape) * df.columns - mol_ions[np.newaxis].T * np
        .ones(df.shape)) < 1
    d = (df.values * d).sum(axis=1)
    return Trace(d, df.index, name='m-' + str(minus))