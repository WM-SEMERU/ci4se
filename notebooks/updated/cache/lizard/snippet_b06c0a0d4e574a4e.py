def _country_level_time_zones_for_number(numobj):
    cc = str(numobj.country_code)
    for prefix_len in range(TIMEZONE_LONGEST_PREFIX, 0, -1):
        prefix = cc[:1 + prefix_len]
        if prefix in TIMEZONE_DATA:
            return TIMEZONE_DATA[prefix]
    return _UNKNOWN_TIME_ZONE_LIST