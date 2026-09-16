def url_for(self, resource, **values):
    endpoint = resource.endpoint
    if self.blueprint:
        endpoint = '{0}.{1}'.format(self.blueprint.name, endpoint)
    return url_for(endpoint, **values)