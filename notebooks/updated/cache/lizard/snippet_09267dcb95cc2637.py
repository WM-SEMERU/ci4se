def _parse_datetime_default_value(property_name, default_value_string):
    parsed_value = time.strptime(default_value_string, ORIENTDB_DATETIME_FORMAT
        )
    return datetime.datetime(parsed_value.tm_year, parsed_value.tm_mon,
        parsed_value.tm_mday, parsed_value.tm_hour, parsed_value.tm_min,
        parsed_value.tm_sec, 0, None)