def iter_all(self, recursive=False, path=None, key='path'):
    if isinstance(key, six.string_types) or key is None:
        if key in _iter_emitters:
            emitter = _iter_emitters[key]
        else:
            raise ValueError('Invalid key {!r}'.format(key))
    else:
        emitter = lambda k, v, _, f=key: (f(k, v), v)
    for p, obj in self._get_path_iterator(recursive=recursive, path=path):
        yield emitter(p, obj, self.settings.str_path_separator)