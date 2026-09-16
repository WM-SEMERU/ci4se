def metric(self):
    if self._metric is None:
        _log.debug('Computing and caching operator basis metric')
        self._metric = np.matrix([[(j.dag() * k).tr() for k in self.ops] for
            j in self.ops])
    return self._metric