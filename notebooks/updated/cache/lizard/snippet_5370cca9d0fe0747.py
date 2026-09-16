def normalize(self):
    for attr in self._avm:
        val = self._avm[attr]
        if isinstance(val, Conjunction):
            val.normalize()
            if len(val.terms) == 1 and isinstance(val.terms[0], AVM):
                self._avm[attr] = val.terms[0]
        elif isinstance(val, AVM):
            val.normalize()