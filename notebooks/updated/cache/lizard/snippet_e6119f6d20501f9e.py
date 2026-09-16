def indicator_pivot(self, indicator_resource):
    resource = self.copy()
    resource._request_uri = '{}/{}'.format(indicator_resource.request_uri,
        resource._request_uri)
    return resource