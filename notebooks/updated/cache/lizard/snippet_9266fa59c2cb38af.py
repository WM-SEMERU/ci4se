def add_mvn(self, name, input_name, output_name, across_channels=True,
    normalize_variance=True, epsilon=1e-05):
    spec = self.spec
    nn_spec = self.nn_spec
    spec_layer = nn_spec.layers.add()
    spec_layer.name = name
    spec_layer.input.append(input_name)
    spec_layer.output.append(output_name)
    spec_layer_params = spec_layer.mvn
    spec_layer_params.acrossChannels = across_channels
    spec_layer_params.normalizeVariance = normalize_variance
    spec_layer_params.epsilon = epsilon