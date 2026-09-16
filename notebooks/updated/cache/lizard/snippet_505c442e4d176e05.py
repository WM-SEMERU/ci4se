def raise_error_unsupported_categorical_option(option_name, option_value,
    layer_type, layer_name):
    raise RuntimeError('Unsupported option %s=%s in layer %s(%s)' % (
        option_name, option_value, layer_type, layer_name))