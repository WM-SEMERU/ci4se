def load(self, url, offset=0, length=-1):
    file_only = url.startswith(('/', '.'))
    filename = from_file_url(url)
    if filename != url:
        file_only = True
        url = filename
    try:
        afile = open(url, 'rb')
    except IOError:
        if file_only:
            raise
        return super(LocalFileLoader, self).load(url, offset, length)
    if offset > 0:
        afile.seek(offset)
    if length >= 0:
        return LimitReader(afile, length)
    else:
        return afile