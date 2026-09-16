def count(self):
    ids, _, ngroups = self.grouper.group_info
    val = self.obj.get_values()
    mask = (ids != -1) & ~isna(val)
    ids = ensure_platform_int(ids)
    minlength = ngroups or 0
    out = np.bincount(ids[mask], minlength=minlength)
    return Series(out, index=self.grouper.result_index, name=self.
        _selection_name, dtype='int64')