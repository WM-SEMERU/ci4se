def _needs_reindex_multi(self, axes, method, level):
    return (com.count_not_none(*axes.values()) == self._AXIS_LEN and method is
        None and level is None and not self._is_mixed_type)