def eradicate_pgroup(self, pgroup, **kwargs):
    eradicate = {'eradicate': True}
    eradicate.update(kwargs)
    return self._request('DELETE', 'pgroup/{0}'.format(pgroup), eradicate)