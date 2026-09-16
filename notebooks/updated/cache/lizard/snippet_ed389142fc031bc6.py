def set_levels(self, levels, level=None, inplace=False, verify_integrity=True):
    if is_list_like(levels) and not isinstance(levels, Index):
        levels = list(levels)
    if level is not None and not is_list_like(level):
        if not is_list_like(levels):
            raise TypeError('Levels must be list-like')
        if is_list_like(levels[0]):
            raise TypeError('Levels must be list-like')
        level = [level]
        levels = [levels]
    elif level is None or is_list_like(level):
        if not is_list_like(levels) or not is_list_like(levels[0]):
            raise TypeError('Levels must be list of lists-like')
    if inplace:
        idx = self
    else:
        idx = self._shallow_copy()
    idx._reset_identity()
    idx._set_levels(levels, level=level, validate=True, verify_integrity=
        verify_integrity)
    if not inplace:
        return idx