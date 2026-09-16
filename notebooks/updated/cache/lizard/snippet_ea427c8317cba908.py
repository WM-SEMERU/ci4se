def add_many(self, data):
    assert isinstance(data, list), 'Incorrect format. Expecting list.'
    if self.is_none or self.is_any:
        self.clear()
        self.data[self.typeof] = []
    data = element_resolver(data, do_raise=False)
    self.data[self.typeof] = data