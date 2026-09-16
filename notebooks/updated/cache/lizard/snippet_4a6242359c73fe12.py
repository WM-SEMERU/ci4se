def _options(self, **kwargs):

    def _format_fq(d):
        for k, v in d.items():
            if isinstance(v, list):
                d[k] = ' '.join(map(lambda x: '"' + x + '"', v))
            else:
                d[k] = '"' + v + '"'
        values = []
        for k, v in d.items():
            value = '%s:(%s)' % (k, v)
            values.append(value)
        values = ' AND '.join(values)
        return values
    kwargs = self._utf8_encode(kwargs)
    kwargs = self._bool_encode(kwargs)
    values = ''
    for k, v in kwargs.items():
        if k is 'fq' and isinstance(v, dict):
            v = _format_fq(v)
        elif isinstance(v, list):
            v = ','.join(v)
        values += '%s=%s&' % (k, v)
    return values