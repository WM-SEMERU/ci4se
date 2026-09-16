def guess_encoding(request):
    ctype = request.headers.get('content-type')
    if not ctype:
        LOGGER.warning('%s: no content-type; headers are %s', request.url,
            request.headers)
        return 'utf-8'
    match = re.search('charset=([^ ;]*)(;| |$)', ctype)
    if match:
        return match[1]
    if ctype.startswith('text/html'):
        return 'iso-8859-1'
    return 'utf-8'