def _add_mac_token(self, uri, http_method='GET', body=None, headers=None,
    token_placement=AUTH_HEADER, ext=None, **kwargs):
    if token_placement != AUTH_HEADER:
        raise ValueError('Invalid token placement.')
    headers = tokens.prepare_mac_header(self.access_token, uri, self.
        mac_key, http_method, headers=headers, body=body, ext=ext,
        hash_algorithm=self.mac_algorithm, **kwargs)
    return uri, headers, body