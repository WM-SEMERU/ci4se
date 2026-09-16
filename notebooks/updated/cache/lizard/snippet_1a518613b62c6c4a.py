def _unpack_token_compact(token):
    if isinstance(token, (str, unicode)):
        token = token.encode('utf-8')
    try:
        signing_input, crypto_segment = token.rsplit(b'.', 1)
        header_segment, payload_segment = signing_input.split(b'.', 1)
    except ValueError:
        raise DecodeError('Not enough segments')
    try:
        header_data = base64url_decode(header_segment)
    except (TypeError, binascii.Error):
        raise DecodeError('Invalid header padding')
    try:
        header = json.loads(header_data.decode('utf-8'))
    except ValueError as e:
        raise DecodeError('Invalid header string: %s' % e)
    if not isinstance(header, Mapping):
        raise DecodeError('Invalid header string: must be a json object')
    try:
        payload_data = base64url_decode(payload_segment)
    except (TypeError, binascii.Error):
        raise DecodeError('Invalid payload padding')
    try:
        payload = json.loads(payload_data.decode('utf-8'))
    except ValueError as e:
        raise DecodeError('Invalid payload string: %s' % e)
    try:
        signature = base64url_decode(crypto_segment)
    except (TypeError, binascii.Error):
        raise DecodeError('Invalid crypto padding')
    return header, payload, signature, signing_input