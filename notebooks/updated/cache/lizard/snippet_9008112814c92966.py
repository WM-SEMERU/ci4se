def convert_dense(builder, layer, input_names, output_names, keras_layer):
    input_name, output_name = input_names[0], output_names[0]
    has_bias = keras_layer.bias
    W = keras_layer.get_weights()[0].T
    Wb = keras_layer.get_weights()[1].T if has_bias else None
    builder.add_inner_product(name=layer, W=W, b=Wb, input_channels=
        keras_layer.input_dim, output_channels=keras_layer.output_dim,
        has_bias=has_bias, input_name=input_name, output_name=output_name)