def _dense_var_to_tensor(self, dtype=None, name=None, as_ref=False):
    if _enclosing_tpu_context() is None:
        if hasattr(self._primary_var, '_dense_var_to_tensor'):
            return self._primary_var._dense_var_to_tensor(dtype, name, as_ref)
        else:
            return ops.convert_to_tensor(self._primary_var)
    if dtype is not None and dtype != self.dtype:
        return NotImplemented
    if as_ref:
        return self.handle
    else:
        return self.read_value()