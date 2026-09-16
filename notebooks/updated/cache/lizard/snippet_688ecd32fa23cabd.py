def parse_authorization_header(value):
    if not value:
        return
    value = wsgi_to_bytes(value)
    try:
        auth_type, auth_info = value.split(None, 1)
        auth_type = auth_type.lower()
    except ValueError:
        return
    if auth_type == b'basic':
        try:
            username, password = base64.b64decode(auth_info).split(b':', 1)
        except Exception:
            return
        return Authorization('basic', {'username': to_unicode(username,
            _basic_auth_charset), 'password': to_unicode(password,
            _basic_auth_charset)})
    elif auth_type == b'digest':
        auth_map = parse_dict_header(auth_info)
        for key in ('username', 'realm', 'nonce', 'uri', 'response'):
            if key not in auth_map:
                return
        if 'qop' in auth_map:
            if not auth_map.get('nc') or not auth_map.get('cnonce'):
                return
        return Authorization('digest', auth_map)