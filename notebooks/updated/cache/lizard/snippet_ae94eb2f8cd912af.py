def _scale_tensor(tensor, range_min, range_max, scale_min, scale_max):
    if range_min == range_max:
        return tensor
    float_tensor = tf.to_float(tensor)
    scaled_tensor = tf.divide(tf.subtract(float_tensor, range_min) * tf.
        constant(float(scale_max - scale_min)), tf.constant(float(range_max -
        range_min)))
    shifted_tensor = scaled_tensor + tf.constant(float(scale_min))
    return shifted_tensor