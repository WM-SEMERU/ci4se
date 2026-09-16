def add(self, data):
    bfo = BitFieldOperation(self.database, self.key)
    for bit_index in self._get_seeds(data):
        bfo.set('u1', bit_index, 1)
    bfo.execute()