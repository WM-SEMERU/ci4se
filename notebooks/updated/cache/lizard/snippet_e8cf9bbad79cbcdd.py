def platform_versions(klass, account, **kwargs):
    resource = klass.RESOURCE_OPTIONS + 'platform_versions'
    request = Request(account.client, 'get', resource, params=kwargs)
    return Cursor(None, request)