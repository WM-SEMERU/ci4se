def trigger(self):
    self._trigger, value = self.get_attr_from_set(self._trigger, 'trigger')
    return value