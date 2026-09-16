def getInterval(self, alpha):
    dlnl = twosided_cl_to_dlnl(1.0 - alpha)
    lo_lim = self.getDeltaLogLike(dlnl, upper=False)
    hi_lim = self.getDeltaLogLike(dlnl, upper=True)
    return lo_lim, hi_lim