def _pool(input_layer, pool_fn, kernel, stride, edges, name):
    input_layer.get_shape().assert_has_rank(4)
    if input_layer.get_shape().ndims not in (None, 4):
        raise ValueError('Pooling requires a rank 4 tensor: %s' %
            input_layer.get_shape())
    kernel = _kernel(kernel)
    stride = _stride(stride)
    size = [1, kernel[0], kernel[1], 1]
    new_head = pool_fn(input_layer.tensor, size, stride, edges, name=name)
    return input_layer.with_tensor(new_head)