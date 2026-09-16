def localize_file_datasource(file_href, dirs):
    mapnik_requires_absolute_paths = MAPNIK_VERSION < 601
    file_href = urljoin(dirs.source.rstrip('/') + '/', file_href)
    scheme, n, path, p, q, f = urlparse(file_href)
    if scheme in ('http', 'https'):
        scheme, path = '', locally_cache_remote_file(file_href, dirs.cache)
    if scheme not in ('file', ''):
        raise Exception(
            'Datasource file needs to be a working, fetchable resource, not %s'
             % file_href)
    if mapnik_requires_absolute_paths:
        return posixpath.realpath(path)
    else:
        return dirs.output_path(path)