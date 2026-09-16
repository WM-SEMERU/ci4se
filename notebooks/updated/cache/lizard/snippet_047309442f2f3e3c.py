def get_lenet():
    data = mx.symbol.Variable('data')
    conv1 = mx.symbol.CaffeOp(data_0=data, num_weight=2, prototxt=
        'layer{type:"Convolution" convolution_param { num_output: 20 kernel_size: 5 stride: 1} }'
        )
    act1 = mx.symbol.CaffeOp(data_0=conv1, prototxt='layer{type:"TanH"}')
    pool1 = mx.symbol.CaffeOp(data_0=act1, prototxt=
        'layer{type:"Pooling" pooling_param { pool: MAX kernel_size: 2 stride: 2}}'
        )
    conv2 = mx.symbol.CaffeOp(data_0=pool1, num_weight=2, prototxt=
        'layer{type:"Convolution" convolution_param { num_output: 50 kernel_size: 5 stride: 1} }'
        )
    act2 = mx.symbol.CaffeOp(data_0=conv2, prototxt='layer{type:"TanH"}')
    pool2 = mx.symbol.CaffeOp(data_0=act2, prototxt=
        'layer{type:"Pooling" pooling_param { pool: MAX kernel_size: 2 stride: 2}}'
        )
    fc1 = mx.symbol.CaffeOp(data_0=pool2, num_weight=2, prototxt=
        'layer{type:"InnerProduct" inner_product_param{num_output: 500} }')
    act3 = mx.symbol.CaffeOp(data_0=fc1, prototxt='layer{type:"TanH"}')
    fc2 = mx.symbol.CaffeOp(data_0=act3, num_weight=2, prototxt=
        'layer{type:"InnerProduct"inner_product_param{num_output: 10} }')
    if use_caffe_loss:
        label = mx.symbol.Variable('softmax_label')
        lenet = mx.symbol.CaffeLoss(data=fc2, label=label, grad_scale=1,
            name='softmax', prototxt='layer{type:"SoftmaxWithLoss"}')
    else:
        lenet = mx.symbol.SoftmaxOutput(data=fc2, name='softmax')
    return lenet