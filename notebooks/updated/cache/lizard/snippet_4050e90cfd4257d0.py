def parse_request_uri_response(self, uri, state=None, scope=None):
    self.token = parse_implicit_response(uri, state=state, scope=scope)
    self.populate_token_attributes(self.token)
    return self.token