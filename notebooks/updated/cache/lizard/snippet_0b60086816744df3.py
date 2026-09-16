def lookup(val, field=None, use_cache=True):
    import jellyfish
    if field is None:
        if FIPS_RE.match(val):
            field = 'fips'
        elif ABBR_RE.match(val):
            val = val.upper()
            field = 'abbr'
        else:
            val = jellyfish.metaphone(val)
            field = 'name_metaphone'
    cache_key = '%s:%s' % (field, val)
    if use_cache and cache_key in _lookup_cache:
        return _lookup_cache[cache_key]
    for state in STATES_AND_TERRITORIES:
        if val == getattr(state, field):
            _lookup_cache[cache_key] = state
            return state