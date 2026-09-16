def Verify(self, mempool):
    for descriptor in self.Descriptors:
        if not descriptor.Verify():
            return False
    return super(StateTransaction, self).Verify(mempool)