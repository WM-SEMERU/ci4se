def get_current_url(request, ignore_params=None):
    if ignore_params is None:
        ignore_params = set()
    protocol = 'https' if request.is_secure() else 'http'
    service_url = '%s://%s%s' % (protocol, request.get_host(), request.path)
    if request.GET:
        params = copy_params(request.GET, ignore_params)
        if params:
            service_url += '?%s' % urlencode(params)
    return service_url