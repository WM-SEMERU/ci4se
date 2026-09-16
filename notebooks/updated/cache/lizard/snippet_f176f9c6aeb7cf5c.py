def time_zones_for_number(numobj):
    ntype = number_type(numobj)
    if ntype == PhoneNumberType.UNKNOWN:
        return _UNKNOWN_TIME_ZONE_LIST
    elif not is_number_type_geographical(ntype, numobj.country_code):
        return _country_level_time_zones_for_number(numobj)
    return time_zones_for_geographical_number(numobj)