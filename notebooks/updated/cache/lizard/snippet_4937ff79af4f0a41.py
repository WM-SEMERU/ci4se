def momentum(self, exponent=1, errorrequested=True):
    y = self.Intensity * self.q ** exponent
    m = np.trapz(y, self.q)
    if errorrequested:
        err = self.Error * self.q ** exponent
        dm = errtrapz(self.q, err)
        return ErrorValue(m, dm)
    else:
        return m