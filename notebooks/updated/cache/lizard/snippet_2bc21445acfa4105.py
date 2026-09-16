def _get_base_value_unwrapped_as_list(self, entity):
    wrapped = self._get_base_value(entity)
    if self._repeated:
        if wrapped is None:
            return []
        assert isinstance(wrapped, list)
        return [w.b_val for w in wrapped]
    else:
        if wrapped is None:
            return [None]
        assert isinstance(wrapped, _BaseValue)
        return [wrapped.b_val]