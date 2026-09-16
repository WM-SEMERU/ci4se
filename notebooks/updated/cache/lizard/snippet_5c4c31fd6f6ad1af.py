def was_modified_since(header=None, mtime=0, size=0):
    try:
        if header is None:
            raise ValueError
        matches = re.match('^([^;]+)(; length=([0-9]+))?$', header, re.
            IGNORECASE)
        header_mtime = parse_http_date(matches.group(1))
        header_len = matches.group(3)
        if header_len and int(header_len) != size:
            raise ValueError
        if int(mtime) > header_mtime:
            raise ValueError
    except (AttributeError, ValueError, OverflowError):
        return True
    return False