def get_detector(net, prefix, epoch, data_shape, mean_pixels, ctx,
    num_class, nms_thresh=0.5, force_nms=True, nms_topk=400):
    if net is not None:
        if isinstance(data_shape, tuple):
            data_shape = data_shape[0]
        net = get_symbol(net, data_shape, num_classes=num_class, nms_thresh
            =nms_thresh, force_nms=force_nms, nms_topk=nms_topk)
    detector = Detector(net, prefix, epoch, data_shape, mean_pixels, ctx=ctx)
    return detector