def objective(self, params):
    val = self._penalty * np.sum(params ** 2)
    for win, los in self._data:
        val += np.logaddexp(0, -(params[win] - params[los]))
    return val