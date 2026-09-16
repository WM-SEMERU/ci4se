def html_encode(path):
    if sys.version_info > (3, 2, 0):
        return urllib.parse.quote(utils.ensure_string(path))
    else:
        return urllib.quote(utils.ensure_string(path))