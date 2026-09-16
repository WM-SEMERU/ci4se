def uri_read(*args, **kwargs):
    with uri_open(*args, **kwargs) as f:
        content = f.read()
    return content