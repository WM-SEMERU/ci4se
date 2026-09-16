def add_split(self, name, input_name, output_names):
    spec = self.spec
    nn_spec = self.nn_spec
    spec_layer = nn_spec.layers.add()
    spec_layer.name = name
    spec_layer.input.append(input_name)
    spec_layer.output.extend(output_names)
    spec_layer_params = spec_layer.split
    spec_layer_params.nOutputs = len(output_names)