def get_localzone():
    global _cache_tz
    if _cache_tz is None:
        _cache_tz = pytz.timezone(get_localzone_name())
    utils.assert_tz_offset(_cache_tz)
    return _cache_tz