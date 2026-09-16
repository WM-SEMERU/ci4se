def __parse_uri(self):
    if self.scheme:
        scheme = '{}://'.format(self.scheme)
    else:
        scheme = ''
    credentials = self.username or ''
    password = self.password or ''
    if credentials and password:
        credentials = self.username + ':' + self.password
    if credentials:
        credentials += '@'
    if self.port:
        location = '{}:{}'.format(self.host, self.port)
    else:
        location = self.host
    path = self.path or ''
    if self.query:
        query = '?' + self.query
    else:
        query = ''
    if self.fragment:
        fragment = '#' + self.fragment
    else:
        fragment = ''
    return scheme + credentials + location + path + query + fragment