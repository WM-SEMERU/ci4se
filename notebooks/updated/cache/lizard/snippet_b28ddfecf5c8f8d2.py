def _get_grad(net, image, class_id=None, conv_layer_name=None, image_grad=False
    ):
    if image_grad:
        image.attach_grad()
        Conv2D.capture_layer_name = None
        Activation.set_guided_backprop(True)
    else:
        Conv2D.capture_layer_name = conv_layer_name
        Activation.set_guided_backprop(False)
    with autograd.record(train_mode=False):
        out = net(image)
    if class_id == None:
        model_output = out.asnumpy()
        class_id = np.argmax(model_output)
    one_hot_target = mx.nd.one_hot(mx.nd.array([class_id]), 1000)
    out.backward(one_hot_target, train_mode=False)
    if image_grad:
        return image.grad[0].asnumpy()
    else:
        conv_out = Conv2D.conv_output
        return conv_out[0].asnumpy(), conv_out.grad[0].asnumpy()