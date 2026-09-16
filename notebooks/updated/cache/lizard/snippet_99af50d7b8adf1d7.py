def from_api_repr(cls, resource, client):
    project = cls(project_id=resource['projectId'], client=client)
    project.set_properties_from_api_repr(resource)
    return project