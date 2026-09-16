def cast_like(x, y):
    x = tf.convert_to_tensor(x)
    y = tf.convert_to_tensor(y)
    if x.dtype.base_dtype == y.dtype.base_dtype:
        return x
    cast_x = tf.cast(x, y.dtype)
    if cast_x.device != x.device:
        x_name = '(eager Tensor)'
        try:
            x_name = x.name
        except AttributeError:
            pass
        tf.logging.warning("Cast for %s may induce copy from '%s' to '%s'",
            x_name, x.device, cast_x.device)
    return cast_x