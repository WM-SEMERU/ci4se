def revoke_token(self, token, orphan=False, accessor=False):
    if accessor and orphan:
        msg = (
            "revoke_token does not support 'orphan' and 'accessor' flags together"
            )
        raise exceptions.InvalidRequest(msg)
    elif accessor:
        params = {'accessor': token}
        self._adapter.post('/v1/auth/token/revoke-accessor', json=params)
    elif orphan:
        params = {'token': token}
        self._adapter.post('/v1/auth/token/revoke-orphan', json=params)
    else:
        params = {'token': token}
        self._adapter.post('/v1/auth/token/revoke', json=params)