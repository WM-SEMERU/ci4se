def url_to_dir_parts(url, include_protocol=False, include_hostname=False,
    alt_char=False):
    assert isinstance(url, str), 'Expect str. Got {}.'.format(type(url))
    url_split_result = urllib.parse.urlsplit(url)
    parts = []
    if include_protocol:
        parts.append(url_split_result.scheme)
    if include_hostname:
        hostname = url_split_result.hostname
        if url_split_result.port:
            if alt_char:
                port_delim = '+'
            else:
                port_delim = ':'
            hostname = '{0}{1}{2}'.format(hostname, port_delim,
                url_split_result.port)
        parts.append(hostname)
    for path_part in url_split_result.path.split('/'):
        if path_part:
            parts.append(path_part)
    if not url.endswith('/') and parts:
        parts.pop()
    return parts