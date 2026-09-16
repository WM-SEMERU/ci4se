def current_kv_names(sci, app_user, app_name, request=None):
    resolver = sm.getUtility(IRequest, 'sparc.utils.requests.request_resolver')
    req = resolver(request=request)
    kwargs = {'auth': (sci['username'], sci['password'])}
    url = ''.join(['https://', sci['host'], ':', sci['port'],
        '/servicesNS/', app_user, '/', app_name, '/'])
    _return = set()
    r = req.request('get', url + 'storage/collections/config', **kwargs)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    for entry in root.findall('./atom:entry', xml_ns):
        name = entry.find('./atom:title', xml_ns).text
        if not name:
            raise ValueError('unexpectedly found empty collection title')
        _return.add(name)
    return _return