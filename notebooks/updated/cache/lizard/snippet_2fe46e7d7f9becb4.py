def _parse_url(path):
    if sys.version_info[0] < 3:
        o = urlparse(urllib.parse.unquote_plus(path).decode('utf8'))
    else:
        o = urlparse(urllib.parse.unquote_plus(path))
    path = o.path
    args = {}
    multiargs = parse_qs(o.query, keep_blank_values=True)
    for arg, value in list(multiargs.items()):
        args[arg] = value[0]
    return path, args