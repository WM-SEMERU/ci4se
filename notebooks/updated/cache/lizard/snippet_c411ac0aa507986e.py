def initial_populate(self, data):
    if self.config.parsed:
        return False
    self.config.load_from_dict(data)
    return True