def _addRawResult(self, resid, values={}, override=False):
    if override or resid not in self._rawresults.keys():
        self._rawresults[resid] = [values]
    else:
        self._rawresults[resid].append(values)