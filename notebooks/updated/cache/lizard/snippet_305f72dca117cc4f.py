def POST(self, **kwargs):
    r
    for creds in cherrypy.request.lowstate:
        try:
            creds.update({'client': 'runner', 'fun': 'auth.mk_token',
                'kwarg': {'username': creds['username'], 'password': creds[
                'password'], 'eauth': creds['eauth']}})
        except KeyError:
            raise cherrypy.HTTPError(400,
                'Require "username", "password", and "eauth" params')
    return list(self.exec_lowstate())