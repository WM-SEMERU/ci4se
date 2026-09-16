def _parse(data):
    if not data:
        return []
    elif isinstance(data, (tuple, list)):
        return [_parse(subdata) for subdata in data]
    d = {ik: v for k in data.keys() for ik, v in data[k].items()}
    to_parse = dict(d)
    for k, v in to_parse.items():
        if k in {'name', 'display_name',
            'display_name_with_invitation_email_address', 'username',
            'challonge_username'}:
            continue
        if isinstance(v, TEXT_TYPE):
            try:
                dt = iso8601.parse_date(v)
                d[k] = dt.astimezone(tz)
            except iso8601.ParseError:
                try:
                    d[k] = float(v)
                except ValueError:
                    pass
    return d