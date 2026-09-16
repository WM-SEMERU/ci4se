def replace(parent, idx, value, check_value=_NO_VAL):
    if isinstance(parent, dict):
        if idx not in parent:
            raise JSONPatchError('Item does not exist')
    elif isinstance(parent, list):
        idx = int(idx)
        if idx < 0 or idx >= len(parent):
            raise JSONPatchError('List index out of range')
    if check_value is not _NO_VAL:
        if parent[idx] != check_value:
            raise JSONPatchError('Check value did not pass')
    parent[idx] = value