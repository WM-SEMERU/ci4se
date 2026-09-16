def get_available_name(self, name):
    if self.exists(name):
        self.delete(name)
    return name