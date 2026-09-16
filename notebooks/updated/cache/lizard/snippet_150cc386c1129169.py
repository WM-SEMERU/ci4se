def to_uri(url):
    parts = WbUrl.FIRST_PATH.split(url, 1)
    sep = url[len(parts[0])] if len(parts) > 1 else None
    scheme_dom = unquote_plus(parts[0])
    if six.PY2 and isinstance(scheme_dom, six.binary_type):
        if scheme_dom == parts[0]:
            return url
        scheme_dom = scheme_dom.decode('utf-8', 'ignore')
    scheme_dom = scheme_dom.rsplit('/', 1)
    domain = scheme_dom[-1]
    try:
        domain = to_native_str(domain.encode('idna'), 'utf-8')
    except UnicodeError:
        pass
    if len(scheme_dom) > 1:
        url = to_native_str(scheme_dom[0], 'utf-8') + '/' + domain
    else:
        url = domain
    if len(parts) > 1:
        url += sep
        rest = parts[1]
        try:
            rest.encode('ascii')
        except UnicodeEncodeError:
            rest = quote(to_native_str(rest, 'utf-8'))
        url += rest
    return url