def header(self, method, client='htmlshark'):
    return {'token': self._request_token(method, client), 'privacy': 0,
        'uuid': self.session.user, 'clientRevision': grooveshark.const.
        CLIENTS[client]['version'], 'session': self.session.session,
        'client': client, 'country': self.session.country}