def _combine(self, applied):
    applied_example, applied = peek_at(applied)
    coord, dim, positions = self._infer_concat_args(applied_example)
    combined = concat(applied, dim)
    combined = _maybe_reorder(combined, dim, positions)
    if coord is not None:
        combined[coord.name] = coord
    combined = self._maybe_restore_empty_groups(combined)
    combined = self._maybe_unstack(combined)
    return combined