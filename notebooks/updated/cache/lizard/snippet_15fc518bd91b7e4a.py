def factors(self):
    if self._factors is None:
        self._factors = FactorList(self._version, service_sid=self.
            _solution['service_sid'], identity=self._solution['identity'])
    return self._factors