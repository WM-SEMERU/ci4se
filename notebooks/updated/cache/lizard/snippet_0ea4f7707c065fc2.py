def unregister(self, provider):
    if isinstance(provider, type):
        provider = provider()
    if isinstance(provider, DataProvider):
        provider = provider.code
    return self.pop(str(provider).upper(), None)