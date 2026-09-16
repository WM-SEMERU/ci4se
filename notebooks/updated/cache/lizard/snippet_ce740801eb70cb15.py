def create(input_length, hidden_layers, activation='tanh', normalization=None):

    def instantiate(**_):
        return MLP(input_length=input_length, hidden_layers=hidden_layers,
            activation=activation, normalization=normalization)
    return ModelFactory.generic(instantiate)