def v(self, version, max_version=None, **kwargs):
    if not isinstance(version, Version):
        version = self.version_cls(self, version, **kwargs)
    if max_version is not None:
        if not isinstance(max_version, Version):
            max_version = self.version_cls(self, max_version, **kwargs)
        version = VersionRange(version, max_version)
    return version