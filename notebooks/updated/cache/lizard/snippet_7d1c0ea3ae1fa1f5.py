def _determine_current_dimension_size(self, dim_name, max_size):
    if self.dimensions[dim_name] is not None:
        return max_size

    def _find_dim(h5group, dim):
        if dim not in h5group:
            return _find_dim(h5group.parent, dim)
        return h5group[dim]
    dim_variable = _find_dim(self._h5group, dim_name)
    if 'REFERENCE_LIST' not in dim_variable.attrs:
        return max_size
    root = self._h5group['/']
    for ref, _ in dim_variable.attrs['REFERENCE_LIST']:
        var = root[ref]
        for i, var_d in enumerate(var.dims):
            name = _name_from_dimension(var_d)
            if name == dim_name:
                max_size = max(var.shape[i], max_size)
    return max_size