def _maybe_update_cacher(self, clear=False, verify_is_copy=True):
    cacher = getattr(self, '_cacher', None)
    if cacher is not None:
        ref = cacher[1]()
        if ref is None:
            del self._cacher
        else:
            try:
                ref._maybe_cache_changed(cacher[0], self)
            except Exception:
                pass
    if verify_is_copy:
        self._check_setitem_copy(stacklevel=5, t='referant')
    if clear:
        self._clear_item_cache()