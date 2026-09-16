def _apply_subtotals(self, res, include_transforms_for_dims):
    if not include_transforms_for_dims:
        return res
    suppressed_dim_count = 0
    for dim_idx, dim in enumerate(self._all_dimensions):
        if dim.dimension_type == DT.MR_CAT:
            suppressed_dim_count += 1
        if not dim.is_marginable:
            continue
        apparent_dim_idx = dim_idx - suppressed_dim_count
        transform = (dim.has_transforms and apparent_dim_idx in
            include_transforms_for_dims)
        if not transform:
            continue
        insertions = self._insertions(res, dim, dim_idx)
        res = self._update_result(res, insertions, dim_idx)
    return res