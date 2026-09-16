def provide(self, feature_name, provider, *args, **kwargs):
    if not self.allow_replace:
        assert feature_name not in self.providers, 'Duplicate feature: {!r}'.format(
            feature_name)
    if callable(provider) and not isinstance(provider, type):
        self.providers[feature_name] = lambda : provider(*args, **kwargs)
    else:
        self.providers[feature_name] = lambda : provider