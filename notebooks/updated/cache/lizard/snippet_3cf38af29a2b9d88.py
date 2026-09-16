def contact_methods(self, **kwargs):
    endpoint = '{0}/{1}/contact_methods'.format(self.endpoint, self['id'])
    result = self.request('GET', endpoint=endpoint, query_params=kwargs)
    return result['contact_methods']