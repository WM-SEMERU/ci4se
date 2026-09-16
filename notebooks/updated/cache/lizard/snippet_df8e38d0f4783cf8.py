def layers(self):
    layermap = dict()
    for operator in self.ops:
        if hasattr(operator, 'layers'):
            layermap.update(operator.layers())
    return layermap