def put(self, data):
    self._to_put.append(data)
    if self.should_flush():
        self.flush()