def store(self, bank, key, data):
    fun = '{0}.store'.format(self.driver)
    return self.modules[fun](bank, key, data, **self._kwargs)