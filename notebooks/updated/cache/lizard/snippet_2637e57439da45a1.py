def getRemoteName(self, remote):
    if remote.name not in self.registry:
        find = [name for name, ha in self.registry.items() if ha == remote.ha]
        assert len(find) == 1
        return find[0]
    return remote.name