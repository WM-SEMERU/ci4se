def _get_template_for_given_resolution(self, res, return_):
    path = self._layer_files[self._res_indices[res][0]]
    if return_ == 'path':
        return_value = path
    else:
        with rasterio.open(str(path)) as src:
            if return_ == 'meta':
                return_value = src.meta
            elif return_ == 'windows':
                return_value = tuple(src.block_windows())
            else:
                raise ValueError(
                    "'return_' must be 'path', meta' or 'windows'.")
    return return_value