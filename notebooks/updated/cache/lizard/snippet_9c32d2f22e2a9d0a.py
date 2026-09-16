def get(self, stream, fmt='txt', **kwargs):
    sel = ''.join(['&{0}={1}'.format(k, v) for k, v in kwargs.items()])
    url = 'streamds/{0}.{1}?{2}'.format(stream, fmt, sel[1:])
    data = self._db._get_content(url)
    if not data:
        log.error("No data found at URL '%s'." % url)
        return
    if data.startswith('ERROR'):
        log.error(data)
        return
    if fmt == 'txt':
        return read_csv(data)
    return data