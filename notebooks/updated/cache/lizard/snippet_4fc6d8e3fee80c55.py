def lookup_token(self, token=None, accessor=False, wrap_ttl=None):
    token_param = {'token': token}
    accessor_param = {'accessor': token}
    if token:
        if accessor:
            path = '/v1/auth/token/lookup-accessor'
            return self._adapter.post(path, json=accessor_param, wrap_ttl=
                wrap_ttl).json()
        else:
            path = '/v1/auth/token/lookup'
            return self._adapter.post(path, json=token_param).json()
    else:
        path = '/v1/auth/token/lookup-self'
        return self._adapter.get(path, wrap_ttl=wrap_ttl).json()