def url_to_filename(url):
    if url.startswith('/'):
        url = url[1:]
    if url.endswith('/'):
        url = url[:-1]
    url = remove_pardir_symbols(url)
    url = replace_dots_to_underscores_at_last(url)
    return url