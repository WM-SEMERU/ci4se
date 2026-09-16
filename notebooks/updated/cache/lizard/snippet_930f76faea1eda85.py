def require_representation(self, req):
    try:
        type_, subtype, _ = parse_mime_type(req.content_type)
        content_type = '/'.join((type_, subtype))
    except:
        raise falcon.HTTPUnsupportedMediaType(description=
            'Invalid Content-Type header: {}'.format(req.content_type))
    if content_type == 'application/json':
        body = req.stream.read()
        return json.loads(body.decode('utf-8'))
    else:
        raise falcon.HTTPUnsupportedMediaType(description=
            'only JSON supported, got: {}'.format(content_type))