def get_flags():
    flags = unitdata.kv().getrange('reactive.states.', strip=True) or {}
    return sorted(flags.keys())