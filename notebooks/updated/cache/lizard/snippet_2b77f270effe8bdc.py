def get_all_boards(*args, **kwargs):
    https = kwargs.get('https', args[1] if len(args) > 1 else False)
    url_generator = Url(None, https)
    _fetch_boards_metadata(url_generator)
    return get_boards(_metadata.keys(), *args, **kwargs)