def load_data(self, data, callback=None):
    return self.backend.execute(self.value_pickler.load_iterable(data, self
        .session), callback)