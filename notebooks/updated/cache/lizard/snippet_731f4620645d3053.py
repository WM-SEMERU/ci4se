def _validate_auth_scheme(self, req):
    if not req.auth:
        raise AuthRequired(**{'detail': 
            'You must first login to access the requested resource(s). Please retry your request using OAuth 2.0 Bearer Token Authentication as documented in RFC 6750. If you do not have an access_token then request one at the token endpdoint of: %s'
             % self.token_endpoint, 'headers': self._error_headers, 'links':
            'tools.ietf.org/html/rfc6750#section-2.1'})
    elif req.auth_scheme != 'bearer':
        raise AuthRequired(**{'detail':
            'Your Authorization header is using an unsupported authentication scheme. Please modify your scheme to be a string of: "Bearer".'
            , 'headers': self._error_headers, 'links':
            'tools.ietf.org/html/rfc6750#section-2.1'})