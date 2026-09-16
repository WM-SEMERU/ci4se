def respond(self, content=EmptyValue, content_type=EmptyValue,
    always_hash_content=True, ext=None):
    log.debug('generating response header')
    resource = Resource(url=self.resource.url, credentials=self.resource.
        credentials, ext=ext, app=self.parsed_header.get('app', None), dlg=
        self.parsed_header.get('dlg', None), method=self.resource.method,
        content=content, content_type=content_type, always_hash_content=
        always_hash_content, nonce=self.parsed_header['nonce'], timestamp=
        self.parsed_header['ts'])
    mac = calculate_mac('response', resource, resource.gen_content_hash())
    self.response_header = self._make_header(resource, mac, additional_keys
        =['ext'])
    return self.response_header