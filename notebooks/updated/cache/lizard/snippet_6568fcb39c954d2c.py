def get_next(self):
    url = self._get_link('next')
    resource = self.object_type.get_resource_class(self.client)
    resp = resource.perform_api_call(resource.REST_READ, url)
    return List(resp, self.object_type, self.client)