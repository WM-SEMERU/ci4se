def urlunparse(parts):
    scheme, netloc, path, params, query, fragment = parts
    if RE_DRIVE_LETTER_PATH.match(path):
        quoted_path = path[:3] + parse.quote(path[3:])
    else:
        quoted_path = parse.quote(path)
    return parse.urlunparse((parse.quote(scheme), parse.quote(netloc),
        quoted_path, parse.quote(params), parse.quote(query), parse.quote(
        fragment)))