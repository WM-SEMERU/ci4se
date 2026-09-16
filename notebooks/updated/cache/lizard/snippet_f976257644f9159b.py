def drop(self):
    if self._ptr:
        LIBRARY.call(self._drop_ffi_fn, self._ptr)
        self._ptr = None