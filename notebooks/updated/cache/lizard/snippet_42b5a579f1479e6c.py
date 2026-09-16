def str_to_datetime(ts):

    def parse_datetime(ts):
        dt = dateutil.parser.parse(ts)
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=dateutil.tz.tzutc())
        return dt
    if not ts:
        raise InvalidDateError(date=str(ts))
    try:
        m = re.search('^.+?\\s+[\\+\\-\\d]\\d{4}(\\s+.+)$', ts)
        if m:
            ts = ts[:m.start(1)]
        try:
            dt = parse_datetime(ts)
        except ValueError as e:
            m = re.search('^(.+?)\\s+[\\+\\-\\d]\\d{4}.*$', ts)
            if m:
                dt = parse_datetime(m.group(1))
                logger.warning('Date %s str does not have a valid timezone', ts
                    )
                logger.warning('Date converted removing timezone info')
                return dt
            raise e
        return dt
    except ValueError as e:
        raise InvalidDateError(date=str(ts))