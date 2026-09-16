def _map_across_full_axis_select_indices(self, axis, func, indices,
    keep_remaining=False):
    return self.data.apply_func_to_select_indices_along_full_axis(axis,
        func, indices, keep_remaining)