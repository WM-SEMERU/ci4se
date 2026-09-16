def markdown_safe(value, arg=None):
    extensions = arg and arg.split(',') or settings.MARKDOWN_EXTENSIONS
    return _markdown(value, extensions=extensions, safe=True)