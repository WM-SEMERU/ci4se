def request(self, path, args=[], files=[], opts={}, stream=False, decoder=
    None, headers={}, data=None):
    url = self.base + path
    params = []
    params.append(('stream-channels', 'true'))
    for opt in opts.items():
        params.append(opt)
    for arg in args:
        params.append(('arg', arg))
    method = 'post' if files or data else 'get'
    parser = encoding.get_encoding(decoder if decoder else 'none')
    return self._request(method, url, params, parser, stream, files,
        headers, data)