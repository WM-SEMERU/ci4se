def is_legal(self, layers=None):
    if layers is None:
        layers = self.layers
    for layer in layers:
        if layer.is_delete is False:
            if len(layer.input) != layer.input_size:
                return False
            if len(layer.output) < layer.output_size:
                return False
    if self.layer_num(layers) > self.max_layer_num:
        return False
    if self.is_topology(layers) is False:
        return False
    return True