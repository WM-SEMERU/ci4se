def ensure_utf8(app_name_to_show_on_error: str):
    encoding = locale.getpreferredencoding()
    if encoding.lower() != 'utf-8':
        raise OSError('{} works only in UTF-8, but yours is set at {}'.
            format(app_name_to_show_on_error, encoding))