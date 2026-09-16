def _add_alpha(self, data, alpha=None):
    null_mask = alpha if alpha is not None else self._create_alpha(data)
    if np.issubdtype(data.dtype, np.integer):
        null_mask = self._scale_to_dtype(null_mask, data.dtype).astype(data
            .dtype)
    data = xr.concat([data, null_mask], dim='bands')
    return data