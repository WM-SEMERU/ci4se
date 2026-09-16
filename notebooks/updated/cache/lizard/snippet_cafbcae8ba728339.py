def json(self, args=None):
    names = ['identifier', 'abstract', 'keywords']
    out = {key: getattr(self, key) for key in names}
    out.update(self.cf_attrs)
    out = self.format(out, args)
    out['notes'] = self.notes
    out['parameters'] = str({key: {'default': p.default if p.default != p.
        empty else None, 'desc': ''} for key, p in self._sig.parameters.
        items()})
    if six.PY2:
        out = walk_map(out, lambda x: x.decode('utf8') if isinstance(x, six
            .string_types) else x)
    return out