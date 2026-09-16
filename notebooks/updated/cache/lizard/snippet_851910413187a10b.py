def init_dense_weight(layer):
    units = layer.units
    weight = np.eye(units)
    bias = np.zeros(units)
    layer.set_weights((add_noise(weight, np.array([0, 1])), add_noise(bias,
        np.array([0, 1]))))