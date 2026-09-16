def redirect(location=None, internal=False, code=None, headers={},
    add_slash=False, request=None):
    request = request or state.request
    if add_slash:
        if location is None:
            split_url = list(urlparse.urlsplit(request.url))
            new_proto = request.environ.get('HTTP_X_FORWARDED_PROTO',
                split_url[0])
            split_url[0] = new_proto
        else:
            split_url = urlparse.urlsplit(location)
        split_url[2] = split_url[2].rstrip('/') + '/'
        location = urlparse.urlunsplit(split_url)
    if not headers:
        headers = {}
    if internal:
        if code is not None:
            raise ValueError('Cannot specify a code for internal redirects')
        request.environ['pecan.recursive.context'] = request.context
        raise ForwardRequestException(location)
    if code is None:
        code = 302
    raise exc.status_map[code](location=location, headers=headers)