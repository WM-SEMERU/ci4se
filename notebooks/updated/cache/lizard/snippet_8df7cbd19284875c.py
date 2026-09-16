def subnetpool_create(request, name, prefixes, **kwargs):
    LOG.debug(
        'subnetpool_create(): name=%(name)s, prefixes=%(prefixes)s, kwargs=%(kwargs)s'
        , {'name': name, 'prefixes': prefixes, 'kwargs': kwargs})
    body = {'subnetpool': {'name': name, 'prefixes': prefixes}}
    if 'tenant_id' not in kwargs:
        kwargs['tenant_id'] = request.user.project_id
    body['subnetpool'].update(kwargs)
    subnetpool = neutronclient(request).create_subnetpool(body=body).get(
        'subnetpool')
    return SubnetPool(subnetpool)