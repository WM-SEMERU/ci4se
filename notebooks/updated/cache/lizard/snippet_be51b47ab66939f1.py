def _raveled_index_for_transformed(self, param):
    ravi = self._raveled_index_for(param)
    if self._has_fixes():
        fixes = self._fixes_
        transformed = np.r_[:self.size] - (~fixes).cumsum()
        return transformed[ravi[fixes[ravi]]]
    else:
        return ravi