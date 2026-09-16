def handle_407(self, r):
    num_407_calls = r.request.hooks['response'].count(self.handle_407)
    s_auth = r.headers.get('Proxy-authenticate', '')
    if 'digest' in s_auth.lower() and num_407_calls < 2:
        self.chal = requests.auth.parse_dict_header(s_auth.replace(
            'Digest ', ''))
        r.content
        r.raw.release_conn()
        r.request.headers['Authorization'] = self.build_digest_header(r.
            request.method, r.request.url)
        r.request.send(anyway=True)
        _r = r.request.response
        _r.history.append(r)
        return _r
    return r