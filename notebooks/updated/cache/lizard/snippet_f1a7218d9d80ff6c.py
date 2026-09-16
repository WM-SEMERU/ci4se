def get_resource_from_handle(self, resource_handle, verify_repo=True):
    if verify_repo:
        if resource_handle.variables.get('repository_type') != self.name():
            raise ResourceError(
                'repository_type mismatch - requested %r, repository_type is %r'
                 % (resource_handle.variables['repository_type'], self.name()))
        if resource_handle.variables.get('location') != self.location:
            raise ResourceError(
                'location mismatch - requested %r, repository location is %r '
                 % (resource_handle.variables['location'], self.location))
    resource = self.pool.get_resource_from_handle(resource_handle)
    resource._repository = self
    return resource