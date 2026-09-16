def parse_timestamp(raw_timestamp, use_utc, hints):
    global FACEBOOK_TIMESTAMP_FORMATS
    timestamp_string, offset = raw_timestamp.rsplit(' ', 1)
    if 'UTC+' in offset or 'UTC-' in offset:
        if offset[3] == '-':
            offset = [(-1 * int(x)) for x in offset[4:].split(':')]
        else:
            offset = [int(x) for x in offset[4:].split(':')]
    else:
        offset_hint = hints.get(offset, None)
        if not offset_hint:
            if offset not in TIMEZONE_MAP:
                raise UnexpectedTimeFormatError(raw_timestamp)
            elif len(TIMEZONE_MAP[offset]) > 1:
                raise AmbiguousTimeZoneError(offset, TIMEZONE_MAP[offset])
            offset = list(TIMEZONE_MAP[offset].keys())[0][:2]
        else:
            offset = offset_hint
    if len(offset) == 1:
        offset += [0]
    delta = dt_timedelta(hours=offset[0], minutes=offset[1])
    for number, date_parser in enumerate(_LOCALIZED_DATE_PARSERS):
        timestamp = date_parser.parse(timestamp_string)
        if timestamp is None:
            continue
        if number > 0:
            del FACEBOOK_TIMESTAMP_FORMATS[number]
            FACEBOOK_TIMESTAMP_FORMATS = [date_parser
                ] + FACEBOOK_TIMESTAMP_FORMATS
        break
    else:
        raise UnexpectedTimeFormatError(raw_timestamp)
    if use_utc:
        timestamp -= delta
        return timestamp.replace(tzinfo=pytz.utc)
    else:
        return timestamp.replace(tzinfo=TzInfoByOffset(delta))