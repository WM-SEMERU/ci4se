def generate_batch(im_tensor, im_info):
    data = [im_tensor, im_info]
    data_shapes = [('data', im_tensor.shape), ('im_info', im_info.shape)]
    data_batch = mx.io.DataBatch(data=data, label=None, provide_data=
        data_shapes, provide_label=None)
    return data_batch