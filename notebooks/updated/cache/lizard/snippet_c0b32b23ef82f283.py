def receive_external(self, http_verb, host, url, http_headers):
    if http_verb == 'GET':
        return self.http.get(host + url, headers=http_headers, stream=True)
    else:
        raise ValueError('Unsupported http_verb:' + http_verb)