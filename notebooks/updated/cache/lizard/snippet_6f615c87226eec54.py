def async_get_ac_states(self, uid, limit=1, offset=0, fields='*'):
    return (yield from self._get('/pods/{}/acStates'.format(uid), limit=
        limit, fields=fields, offset=offset))