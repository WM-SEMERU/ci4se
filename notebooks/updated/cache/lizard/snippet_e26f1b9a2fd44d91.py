def mkpath(self, url, path, filename=None, gzip=False):
    if path:
        url = '%s/%s' % (url.rstrip('/'), path.strip('/'))
    if filename:
        url = '%s/%s' % (url, filename.lstrip('/'))
    content_type = mimetypes.guess_type(url)[0]
    if gzip and content_type in mediasync.TYPES_TO_COMPRESS:
        url = '%s.gzt' % url
    cb = msettings['CACHE_BUSTER']
    if cb:
        cb_val = cb(url) if callable(cb) else cb
        url = '%s?%s' % (url, cb_val)
    return msettings['URL_PROCESSOR'](url)