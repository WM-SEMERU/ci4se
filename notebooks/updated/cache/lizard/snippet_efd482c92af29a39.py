def _dict(self, with_name=True):
    d = dict([(k, getattr(self, k)) for k, _, _ in self.name_parts])
    if with_name:
        d['name'] = self.name
        try:
            d['vname'] = self.vname
        except ValueError:
            pass
    return self.clear_dict(d)