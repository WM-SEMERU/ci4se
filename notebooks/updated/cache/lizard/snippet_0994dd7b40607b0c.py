def _expand_slice(self, indices):
    keys = list(self.data.keys())
    expanded = []
    for idx, ind in enumerate(indices):
        if isinstance(ind, slice) and ind.step is not None:
            dim_ind = slice(ind.start, ind.stop)
            if dim_ind == slice(None):
                condition = self._all_condition()
            elif dim_ind.start is None:
                condition = self._upto_condition(dim_ind)
            elif dim_ind.stop is None:
                condition = self._from_condition(dim_ind)
            else:
                condition = self._range_condition(dim_ind)
            dim_vals = unique_iterator(k[idx] for k in keys)
            expanded.append(set([k for k in dim_vals if condition(k)][::int
                (ind.step)]))
        else:
            expanded.append(ind)
    return tuple(expanded)