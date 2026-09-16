def policy_net(rng_key, batch_observations_shape, num_actions,
    bottom_layers=None):
    if bottom_layers is None:
        bottom_layers = []
    bottom_layers.extend([layers.Dense(num_actions), layers.LogSoftmax()])
    net = layers.Serial(*bottom_layers)
    return net.initialize(batch_observations_shape, rng_key), net