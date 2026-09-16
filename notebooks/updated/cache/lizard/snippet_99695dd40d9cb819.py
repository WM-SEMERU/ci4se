def add_format(mimetype, format, requires_context=False):
    global formats
    global ctxless_mimetypes
    global all_mimetypes
    formats[mimetype] = format
    if not requires_context:
        ctxless_mimetypes.append(mimetype)
    all_mimetypes.append(mimetype)