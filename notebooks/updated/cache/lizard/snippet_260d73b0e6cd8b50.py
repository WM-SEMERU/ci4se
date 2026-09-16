def get_resource(self, resource_key, repository_type, location, **variables):
    path = '%s@%s' % (repository_type, location)
    repo = self.get_repository(path)
    resource = repo.get_resource(**variables)
    return resource