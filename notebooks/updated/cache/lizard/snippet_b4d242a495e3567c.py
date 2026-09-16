def describe_api_resource(restApiId, path, region=None, key=None, keyid=
    None, profile=None):
    r = describe_api_resources(restApiId, region=region, key=key, keyid=
        keyid, profile=profile)
    resources = r.get('resources')
    if resources is None:
        return r
    for resource in resources:
        if resource['path'] == path:
            return {'resource': resource}
    return {'resource': None}