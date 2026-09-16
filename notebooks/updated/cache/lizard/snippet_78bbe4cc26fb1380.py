def multi_layer_feature(body, from_layers, num_filters, strides, pads,
    min_filter=128):
    assert len(from_layers) > 0
    assert isinstance(from_layers[0], str) and len(from_layers[0].strip()) > 0
    assert len(from_layers) == len(num_filters) == len(strides) == len(pads)
    internals = body.get_internals()
    layers = []
    for k, params in enumerate(zip(from_layers, num_filters, strides, pads)):
        from_layer, num_filter, s, p = params
        if from_layer.strip():
            layer = internals[from_layer.strip() + '_output']
            layers.append(layer)
        else:
            assert len(layers) > 0
            assert num_filter > 0
            layer = layers[-1]
            num_1x1 = max(min_filter, num_filter // 2)
            conv_1x1 = conv_act_layer(layer, 'multi_feat_%d_conv_1x1' % k,
                num_1x1, kernel=(1, 1), pad=(0, 0), stride=(1, 1), act_type
                ='relu')
            conv_3x3 = conv_act_layer(conv_1x1, 'multi_feat_%d_conv_3x3' %
                k, num_filter, kernel=(3, 3), pad=(p, p), stride=(s, s),
                act_type='relu')
            layers.append(conv_3x3)
    return layers