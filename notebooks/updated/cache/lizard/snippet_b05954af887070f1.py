def layers(self):
    layer = ['NONE'] * len(self.entities)
    for i, e in enumerate(self.entities):
        if hasattr(e, 'layer'):
            layer[i] = str(e.layer)
    return layer