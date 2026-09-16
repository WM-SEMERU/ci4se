def save(thing, url_or_handle, **kwargs):
    is_handle = hasattr(url_or_handle, 'write') and hasattr(url_or_handle,
        'name')
    if is_handle:
        _, ext = os.path.splitext(url_or_handle.name)
    else:
        _, ext = os.path.splitext(url_or_handle)
    if not ext:
        raise RuntimeError('No extension in URL: ' + url_or_handle)
    if ext in savers:
        saver = savers[ext]
        if is_handle:
            saver(thing, url_or_handle, **kwargs)
        else:
            with write_handle(url_or_handle) as handle:
                saver(thing, handle, **kwargs)
    else:
        saver_names = [(key, fn.__name__) for key, fn in savers.items()]
        message = "Unknown extension '{}', supports {}."
        raise ValueError(message.format(ext, saver_names))