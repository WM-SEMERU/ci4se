def set_index(self, keys, drop=True, append=False, inplace=False,
    verify_integrity=False):
    if drop is True:
        try:
            assert type(keys) is not str
            dropped_cols = set(keys)
        except (TypeError, AssertionError):
            dropped_cols = set([keys])
    if not self._required_cols <= set(self.columns) - set(dropped_cols):
        raise PhysicalMeaning(
            'You drop a column that is needed to be a physical meaningful description of a molecule.'
            )
    if inplace:
        self._frame.set_index(keys, drop=drop, append=append, inplace=
            inplace, verify_integrity=verify_integrity)
    else:
        new = self._frame.set_index(keys, drop=drop, append=append, inplace
            =inplace, verify_integrity=verify_integrity)
        return self.__class__(new, _metadata=self._metadata, metadata=self.
            metadata)