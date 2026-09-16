def fetch(self, bank, key):
    fun = '{0}.fetch'.format(self.driver)
    return self.modules[fun](bank, key, **self._kwargs)