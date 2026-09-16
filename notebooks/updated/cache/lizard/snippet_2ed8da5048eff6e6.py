def _parse_body(self, robj, response, expected_statuses):
    if response is None:
        return None
    status, headers, data = response
    if not status:
        m = 'Could not contact Riak Server: http://{0}:{1}!'.format(self.
            _node.host, self._node.http_port)
        raise RiakError(m)
    self.check_http_code(status, expected_statuses)
    if 'x-riak-vclock' in headers:
        robj.vclock = VClock(headers['x-riak-vclock'], 'base64')
    if status == 404:
        robj.siblings = []
        return None
    elif status == 201:
        robj.key = headers['location'].strip().split('/')[-1]
    elif status == 300:
        ctype, params = parse_header(headers['content-type'])
        if ctype == 'multipart/mixed':
            if six.PY3:
                data = bytes_to_str(data)
            boundary = re.compile('\r?\n--%s(?:--)?\r?\n' % re.escape(
                params['boundary']))
            parts = [message_from_string(p) for p in re.split(boundary,
                data)[1:-1]]
            robj.siblings = [self._parse_sibling(RiakContent(robj), part.
                items(), part.get_payload()) for part in parts]
            if robj.resolver is not None:
                robj.resolver(robj)
            return robj
        else:
            raise Exception('unexpected sibling response format: {0}'.
                format(ctype))
    robj.siblings = [self._parse_sibling(RiakContent(robj), headers.items(),
        data)]
    return robj