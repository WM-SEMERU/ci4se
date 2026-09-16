def squash_sequence(input_layer):
    timesteps = len(input_layer.sequence)
    if not timesteps:
        raise ValueError('Empty tensor sequence.')
    elif timesteps == 1:
        result = input_layer.sequence[0]
    else:
        result = tf.concat(input_layer.sequence, 0)
    return input_layer.with_tensor(result).with_defaults(unroll=timesteps)