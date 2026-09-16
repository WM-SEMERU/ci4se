def ntoreturn(self):
    if not self._counters_calculated:
        self._counters_calculated = True
        self._extract_counters()
    return self._ntoreturn