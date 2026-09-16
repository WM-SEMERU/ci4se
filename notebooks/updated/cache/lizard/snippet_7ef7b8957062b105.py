def _replace_layer(self, layer_id, new_layer):
    old_layer = self.layer_list[layer_id]
    new_layer.input = old_layer.input
    new_layer.output = old_layer.output
    new_layer.output.shape = new_layer.output_shape
    self.layer_list[layer_id] = new_layer
    self.layer_to_id[new_layer] = layer_id
    self.layer_to_id.pop(old_layer)