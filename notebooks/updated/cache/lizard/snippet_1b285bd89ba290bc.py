def add_layer(self, obj=None):
    new_layer = Layer()
    if obj:
        new_layer.merge(obj)
    self.layers.append(new_layer)