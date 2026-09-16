def check_bewit(url, credential_lookup, now=None):
    raw_bewit, stripped_url = strip_bewit(url)
    bewit = parse_bewit(raw_bewit)
    try:
        credentials = credential_lookup(bewit.id)
    except LookupError:
        raise CredentialsLookupError('Could not find credentials for ID {0}'
            .format(bewit.id))
    res = Resource(url=stripped_url, method='GET', credentials=credentials,
        timestamp=bewit.expiration, nonce='', ext=bewit.ext)
    mac = calculate_mac('bewit', res, None)
    mac = mac.decode('ascii')
    if not strings_match(mac, bewit.mac):
        raise MacMismatch(
            'bewit with mac {bewit_mac} did not match expected mac {expected_mac}'
            .format(bewit_mac=bewit.mac, expected_mac=mac))
    if now is None:
        now = utc_now()
    if int(bewit.expiration) < now:
        raise TokenExpired(
            'bewit with UTC timestamp {ts} has expired; it was compared to {now}'
            .format(ts=bewit.expiration, now=now), localtime_in_seconds=now,
            www_authenticate='')
    return True