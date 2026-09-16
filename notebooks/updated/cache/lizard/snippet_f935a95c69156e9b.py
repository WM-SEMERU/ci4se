def MakePmfFromDict(d, name=''):
    pmf = Pmf(d, name)
    pmf.Normalize()
    return pmf