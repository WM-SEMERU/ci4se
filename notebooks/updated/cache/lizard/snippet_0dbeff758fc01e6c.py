def require_dataset(self, name, shape, dtype=None, exact=False, **kwargs):
    return self._write_op(self._require_dataset_nosync, name, shape=shape,
        dtype=dtype, exact=exact, **kwargs)