def is_image(self, key):
    data = self.model.get_data()
    return isinstance(data[key], Image)