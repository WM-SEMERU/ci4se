def tseries_between(self, tstart=None, tend=None):
    if self.tseries is None:
        return None
    ndat = self.tseries.shape[0]
    if tstart is None:
        istart = 0
    else:
        igm = 0
        igp = ndat - 1
        while igp - igm > 1:
            istart = igm + (igp - igm) // 2
            if self.tseries.iloc[istart]['t'] >= tstart:
                igp = istart
            else:
                igm = istart
        istart = igp
    if tend is None:
        iend = None
    else:
        igm = 0
        igp = ndat - 1
        while igp - igm > 1:
            iend = igm + (igp - igm) // 2
            if self.tseries.iloc[iend]['t'] > tend:
                igp = iend
            else:
                igm = iend
        iend = igm + 1
    return self.tseries.iloc[istart:iend]