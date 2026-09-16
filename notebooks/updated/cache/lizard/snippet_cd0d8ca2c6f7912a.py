def convert_convolution(node, **kwargs):
    name, input_nodes, attrs = get_inputs(node, kwargs)
    kernel_dims = list(parse_helper(attrs, 'kernel'))
    stride_dims = list(parse_helper(attrs, 'stride', [1, 1]))
    pad_dims = list(parse_helper(attrs, 'pad', [0, 0]))
    num_group = int(attrs.get('num_group', 1))
    dilations = list(parse_helper(attrs, 'dilate', [1, 1]))
    pad_dims = pad_dims + pad_dims
    conv_node = onnx.helper.make_node('Conv', inputs=input_nodes, outputs=[
        name], kernel_shape=kernel_dims, strides=stride_dims, dilations=
        dilations, pads=pad_dims, group=num_group, name=name)
    return [conv_node]