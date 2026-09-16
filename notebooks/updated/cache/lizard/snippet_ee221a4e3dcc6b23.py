def createInstance(self, codec=None):
    if type(self.klass) is type:
        return self.klass.__new__(self.klass)
    return self.klass()