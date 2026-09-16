def peek_path_info(environ, charset='utf-8', errors='replace'):
    segments = environ.get('PATH_INFO', '').lstrip('/').split('/', 1)
    if segments:
        return to_unicode(wsgi_get_bytes(segments[0]), charset, errors,
            allow_none_charset=True)