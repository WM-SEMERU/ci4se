def ref(self):
    self._refs = [r for r in self._refs if r() is not None]
    ref = self._refs[0]() if self._refs else None
    if ref is not None:
        return ref
    else:
        raise RuntimeError('No reference for available for GLShared')