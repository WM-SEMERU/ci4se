def config_items(self, sortkey=False):
    if sortkey:
        items = sorted(self.items())
    else:
        items = self.items()
    for k, v in items:
        if isinstance(v, ConfigTree):
            for k2, v2 in v.config_items(sortkey):
                yield k + '.' + k2, v2
        else:
            yield k, v