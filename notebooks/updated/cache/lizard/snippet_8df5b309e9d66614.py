def get_resources_for_api_version(self, prefix, group, version, preferred):
    resources = defaultdict(list)
    subresources = {}
    path = '/'.join(filter(None, [prefix, group, version]))
    resources_response = load_json(self.client.request('GET', path))[
        'resources']
    resources_raw = list(filter(lambda resource: '/' not in resource['name'
        ], resources_response))
    subresources_raw = list(filter(lambda resource: '/' in resource['name'],
        resources_response))
    for subresource in subresources_raw:
        resource, name = subresource['name'].split('/')
        if not subresources.get(resource):
            subresources[resource] = {}
        subresources[resource][name] = subresource
    for resource in resources_raw:
        for key in ('prefix', 'group', 'api_version', 'client', 'preferred'):
            resource.pop(key, None)
        resourceobj = Resource(prefix=prefix, group=group, api_version=
            version, client=self.client, preferred=preferred, subresources=
            subresources.get(resource['name']), **resource)
        resources[resource['kind']].append(resourceobj)
        resource_list = ResourceList(self.client, group=group, api_version=
            version, base_kind=resource['kind'])
        resources[resource_list.kind].append(resource_list)
    return resources