def all_hermitian(self):
    if self._all_hermitian is None:
        _log.debug('Testing and caching if all basis operator are hermitian')
        self._all_hermitian = all(is_hermitian(op) for op in self.ops)
    return self._all_hermitian