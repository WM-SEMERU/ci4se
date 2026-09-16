def parse_gntp(data, password=None):
    data = gntp.shim.u(data)
    match = GNTP_INFO_LINE_SHORT.match(data)
    if not match:
        raise errors.ParseError('INVALID_GNTP_INFO')
    info = match.groupdict()
    if info['messagetype'] == 'REGISTER':
        return GNTPRegister(data, password=password)
    elif info['messagetype'] == 'NOTIFY':
        return GNTPNotice(data, password=password)
    elif info['messagetype'] == 'SUBSCRIBE':
        return GNTPSubscribe(data, password=password)
    elif info['messagetype'] == '-OK':
        return GNTPOK(data)
    elif info['messagetype'] == '-ERROR':
        return GNTPError(data)
    raise errors.ParseError('INVALID_GNTP_MESSAGE')