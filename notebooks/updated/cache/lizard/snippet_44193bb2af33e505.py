def save_json(val, pretty=False, sort=True, encoder=None):
    if encoder is None:
        encoder = DateTimeEncoder
    if pretty:
        data = json.dumps(val, indent=4, separators=(',', ': '), sort_keys=
            sort, cls=encoder)
    else:
        data = json.dumps(val, separators=(',', ':'), sort_keys=sort, cls=
            encoder)
    if not sys.version_info > (3, 0) and isinstance(data, str):
        data = data.decode('utf-8')
    return data