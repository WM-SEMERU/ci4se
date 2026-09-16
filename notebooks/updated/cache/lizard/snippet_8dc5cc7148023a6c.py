def reload(self):
    new_model = self.collection.get(self.id)
    self.attrs = new_model.attrs