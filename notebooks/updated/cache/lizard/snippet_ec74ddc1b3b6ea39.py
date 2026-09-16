def replace(self, **kwargs):
    if 'usage_key' in kwargs:
        for attr in self.USAGE_KEY_ATTRS:
            kwargs.pop(attr, None)
    else:
        kwargs['usage_key'] = self.usage_key.replace(**{key: kwargs.pop(key
            ) for key in self.USAGE_KEY_ATTRS if key in kwargs})
    return super(AsideUsageKeyV2, self).replace(**kwargs)