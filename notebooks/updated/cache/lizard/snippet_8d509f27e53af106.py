def show_release_file(root, request):
    settings = request.registry.settings
    whlify = asbool(settings.get('pyshop.mirror.wheelify', '0'))
    session = DBSession()
    f = ReleaseFile.by_id(session, int(request.matchdict['file_id']))
    whlify = whlify and f.package_type == 'sdist'
    filename = f.filename_whlified if whlify else f.filename
    url = f.url
    if url and url.startswith('http://pypi.python.org'):
        url = 'https' + url[4:]
    rv = {'url': url, 'filename': filename, 'original': f.filename,
        'whlify': whlify}
    f.downloads += 1
    f.release.downloads += 1
    f.release.package.downloads += 1
    session.add(f.release.package)
    session.add(f.release)
    session.add(f)
    request.response.etag = f.md5_digest
    request.response.cache_control = 'max-age=31557600, public'
    request.response.date = datetime.datetime.utcnow()
    return rv