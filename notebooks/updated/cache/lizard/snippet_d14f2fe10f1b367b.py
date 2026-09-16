def delete(self):
    self._engine.data[self.typeof] = [loopback for loopback in self._engine
        .data.get(self.typeof, []) if loopback.get('address') != self.address]
    self._engine.update()