def allow_client_outgoing(self, application_sid, **kwargs):
    scope = ScopeURI('client', 'outgoing', {'appSid': application_sid})
    if kwargs:
        scope.add_param('appParams', urlencode(kwargs, doseq=True))
    self.capabilities['outgoing'] = scope