def lookup(self, name, version=None):
    versions = self.get(name)
    if not versions:
        return None
    if version:
        return versions[version]
    return versions[max(versions)]