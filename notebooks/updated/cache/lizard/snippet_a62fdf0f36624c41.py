def _compute_bounds(self, axis, view):
    if self._bounds is None and self._pos is not None:
        pos = self._pos
        self._bounds = [(pos[:, (d)].min(), pos[:, (d)].max()) for d in
            range(pos.shape[1])]
    if self._bounds is None:
        return
    elif axis < len(self._bounds):
        return self._bounds[axis]
    else:
        return 0, 0