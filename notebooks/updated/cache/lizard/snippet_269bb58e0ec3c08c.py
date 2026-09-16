def patch_to_conflict_set(patch):
    patch_type, patched_key, value = patch
    if isinstance(patched_key, list):
        key_path = tuple(patched_key)
    else:
        key_path = tuple(k for k in patched_key.split('.') if k)
    conflicts = set()
    if patch_type == REMOVE:
        conflict_type = ConflictType.REMOVE_FIELD
        for key, obj in value:
            conflicts.add(Conflict(conflict_type, key_path + (key,), None))
    elif patch_type == CHANGE:
        conflict_type = ConflictType.SET_FIELD
        first_val, second_val = value
        conflicts.add(Conflict(conflict_type, key_path, second_val))
    elif patch_type == ADD:
        conflict_type = ConflictType.SET_FIELD
        for key, obj in value:
            conflicts.add(Conflict(conflict_type, key_path + (key,), obj))
    return conflicts