def load(self, **kwargs):
    if LooseVersion(self.tmos_ver) == LooseVersion('11.6.0'):
        return self._load_11_6(**kwargs)
    else:
        return super(Rule, self)._load(**kwargs)