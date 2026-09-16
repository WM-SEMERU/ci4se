def _add_tzinfo(self, datetime_obj, tz_string):
    if datetime_obj is None:
        return None
    tzinfo_match = tz.gettz(tz_string)
    return datetime_obj.replace(tzinfo=tzinfo_match)