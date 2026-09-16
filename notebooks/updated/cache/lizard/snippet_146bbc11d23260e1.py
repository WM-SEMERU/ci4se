def _guess_type(val):
    if isinstance(val, bool):
        return 'choice'
    elif isinstance(val, int):
        return 'number'
    elif isinstance(val, float):
        return 'number'
    elif isinstance(val, str):
        return 'text'
    elif hasattr(val, 'read'):
        return 'file'
    else:
        return 'text'