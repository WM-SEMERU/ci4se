def make_temp(string, suffix='', decode=True, delete=True):
    ntf = NamedTemporaryFile(suffix=suffix, delete=delete)
    if not isinstance(string, six.binary_type):
        string = string.encode('utf-8')
    if decode:
        ntf.write(base64.b64decode(string))
    else:
        ntf.write(string)
    ntf.seek(0)
    return ntf, ntf.name