def freeze(self, number=None):
    if number is None:
        number = self.head_layers
    for idx, child in enumerate(self.model.children()):
        if idx < number:
            mu.freeze_layer(child)