def GlorotUniformInitializer(out_dim=0, in_dim=1):

    def init(shape, rng):
        fan_in, fan_out = shape[in_dim], shape[out_dim]
        std = np.sqrt(2.0 / (fan_in + fan_out))
        a = np.sqrt(3.0) * std
        return backend.random.uniform(rng, shape, minval=-a, maxval=a)
    return init