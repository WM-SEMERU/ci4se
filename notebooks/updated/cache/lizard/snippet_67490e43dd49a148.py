def get(self, resource_manager, identities):
    m = self.resolve(resource_manager.resource_type)
    params = {}
    client_filter = False
    if m.filter_name:
        if m.filter_type == 'list':
            params[m.filter_name] = identities
        elif m.filter_type == 'scalar':
            assert len(identities) == 1, 'Scalar server side filter'
            params[m.filter_name] = identities[0]
    else:
        client_filter = True
    resources = self.filter(resource_manager, **params)
    if client_filter:
        if all(map(lambda r: isinstance(r, six.string_types), resources)):
            resources = [r for r in resources if r in identities]
        else:
            resources = [r for r in resources if r[m.id] in identities]
    return resources