def variable(self, var_name, shape, init, dt=tf.float32, train=None):
    dt = tf.as_dtype(dt).base_dtype
    if var_name in self.vars:
        v = self.vars[var_name]
        if v.get_shape() != shape:
            raise ValueError(
                'Shape mismatch: %s vs %s. Perhaps a UnboundVariable had incompatible values within a graph.'
                 % (v.get_shape(), shape))
        return v
    elif callable(init):
        if train is None:
            train = _defaults.get('trainable_variables', True)
        variable_collections = _defaults.get('variable_collections', ())
        if tf.GraphKeys.GLOBAL_VARIABLES not in variable_collections:
            variable_collections = list(variable_collections) + [tf.
                GraphKeys.GLOBAL_VARIABLES]
        v = tf.get_variable(var_name, shape=shape, dtype=dt, initializer=
            init, trainable=train, collections=variable_collections)
        self.vars[var_name] = v
        return v
    else:
        v = tf.convert_to_tensor(init, name=var_name, dtype=dt)
        v.get_shape().assert_is_compatible_with(shape)
        self.vars[var_name] = v
        return v