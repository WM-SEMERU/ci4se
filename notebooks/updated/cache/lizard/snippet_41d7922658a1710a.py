def _print(self, *data, **kw):
    sep = kw.pop('sep', ' ')
    end = kw.pop('end', '\n')
    _ = kw.pop('file', None)
    assert not kw, 'Too many keyword-only arguments'
    data = sep.join(map(str, data))
    self._chan.write(data + end)