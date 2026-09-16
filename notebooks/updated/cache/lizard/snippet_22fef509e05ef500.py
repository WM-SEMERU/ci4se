def data_url(content, mimetype=None):
    if isinstance(content, pathlib.Path):
        if not mimetype:
            mimetype = guess_type(content.name)[0]
        with content.open('rb') as fp:
            content = fp.read()
    elif isinstance(content, text_type):
        content = content.encode('utf8')
    return 'data:{0};base64,{1}'.format(mimetype or
        'application/octet-stream', b64encode(content).decode())