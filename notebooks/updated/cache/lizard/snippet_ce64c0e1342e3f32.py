def set(self, path, value):
    _log.debug('ZK: Setting {path} to {value}'.format(path=path, value=value))
    return self.zk.set(path, value)