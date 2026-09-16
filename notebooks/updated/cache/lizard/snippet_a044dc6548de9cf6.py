def degrees_of_freedom(self):
    if len(self._set_xdata) == 0 or len(self._set_ydata) == 0:
        return None
    r = self.studentized_residuals()
    if r == None:
        return
    N = 0.0
    for i in range(len(r)):
        N += len(r[i])
    return N - len(self._pnames)