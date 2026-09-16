def dict(self):
    from collections import OrderedDict
    d = OrderedDict([(p.key, getattr(self, p.key)) for p in self.__mapper__
        .attrs if p.key not in ('data',)])
    if 'list' in self.data:
        d['bundle_count'] = len(self.data['list'])
    else:
        d['bundle_count'] = None
    if self.data:
        for k, v in self.data.items():
            d[k] = v
    return d