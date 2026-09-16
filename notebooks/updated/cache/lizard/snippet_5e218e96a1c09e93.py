def _auth_headers(self):
    if self.token is _NoAuthenticationToken:
        return []
    else:
        if self.token.startswith('Splunk '):
            token = self.token
        else:
            token = 'Splunk %s' % self.token
        return [('Authorization', token)]