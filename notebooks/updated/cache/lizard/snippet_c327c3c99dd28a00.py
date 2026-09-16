def extern_store_f64(self, context_handle, f64):
    c = self._ffi.from_handle(context_handle)
    return c.to_value(f64)