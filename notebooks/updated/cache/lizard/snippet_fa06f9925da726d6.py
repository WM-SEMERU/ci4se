def _has_instance(data, dtype):
    for item in data:
        _, arr = item
        if isinstance(arr, dtype):
            return True
    return False