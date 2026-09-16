def delete(self, kwargs):
    self._to_delete.append(kwargs)
    if self.should_flush():
        self.flush()