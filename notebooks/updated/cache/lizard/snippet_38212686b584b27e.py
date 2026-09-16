def new_address(self, prefix, type, callback=None, errback=None, **kwargs):
    if not self.data:
        raise NetworkException('Network not loaded')
    return Address(self.config, prefix, type, self).create(**kwargs)