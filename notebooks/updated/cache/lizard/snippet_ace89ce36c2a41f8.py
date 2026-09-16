def make_hop_info_from_url(url, verify_reachability=None):
    parsed = urlparse(url)
    username = None if parsed.username is None else unquote(parsed.username)
    password = None if parsed.password is None else unquote(parsed.password)
    try:
        enable_password = parse_qs(parsed.query)['enable_password'][0]
    except KeyError:
        enable_password = None
    hop_info = HopInfo(parsed.scheme, parsed.hostname, username, password,
        parsed.port, enable_password, verify_reachability=verify_reachability)
    if hop_info.is_valid():
        return hop_info
    raise InvalidHopInfoError