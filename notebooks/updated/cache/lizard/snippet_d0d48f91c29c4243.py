def public_copy(self):
    d = dict(chain_code=self._chain_code, depth=self._depth,
        parent_fingerprint=self._parent_fingerprint, child_index=self.
        _child_index, public_pair=self.public_pair())
    return self.__class__(**d)