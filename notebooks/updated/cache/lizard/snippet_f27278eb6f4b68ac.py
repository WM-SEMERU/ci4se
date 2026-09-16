def static_proxy(request):
    normalize = lambda u: '//' + u.split('://')[-1] if '://' in u else u
    url = normalize(request.GET['u'])
    host = '//' + request.get_host()
    static_url = normalize(settings.STATIC_URL)
    for prefix in (host, static_url, '/'):
        if url.startswith(prefix):
            url = url.replace(prefix, '', 1)
    response = ''
    content_type, encoding = mimetypes.guess_type(url)
    if content_type is None:
        content_type = 'application/octet-stream'
    path = finders.find(url)
    if path:
        if isinstance(path, (list, tuple)):
            path = path[0]
        if url.endswith('.htm'):
            static_url = settings.STATIC_URL + os.path.split(url)[0] + '/'
            if not urlparse(static_url).scheme:
                static_url = urljoin(host, static_url)
            base_tag = "<base href='%s'>" % static_url
            with open(path, 'r') as f:
                response = f.read().replace('<head>', '<head>' + base_tag)
        else:
            try:
                with open(path, 'rb') as f:
                    response = f.read()
            except IOError:
                return HttpResponseNotFound()
    return HttpResponse(response, content_type=content_type)