def add_sequence_repeat(self, name, nrep, input_name, output_name):
    spec = self.spec
    nn_spec = self.nn_spec
    spec_layer = nn_spec.layers.add()
    spec_layer.name = name
    spec_layer.input.append(input_name)
    spec_layer.output.append(output_name)
    spec_layer_params = spec_layer.sequenceRepeat
    spec_layer_params.nRepetitions = nrep