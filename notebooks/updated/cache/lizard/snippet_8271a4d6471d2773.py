def open_unknown(self, fullurl, data=None):
    type, url = splittype(fullurl)
    raise IOError('url error', 'unknown url type', type)