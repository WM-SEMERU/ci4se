def valid_padding(in_size, filter_size, stride_size):
    in_height, in_width = in_size
    filter_height, filter_width = filter_size
    stride_height, stride_width = stride_size
    out_height = np.ceil(float(in_height) / float(stride_height))
    out_width = np.ceil(float(in_width) / float(stride_width))
    pad_along_height = int((out_height - 1) * stride_height + filter_height -
        in_height)
    pad_along_width = int((out_width - 1) * stride_width + filter_width -
        in_width)
    pad_top = pad_along_height // 2
    pad_bottom = pad_along_height - pad_top
    pad_left = pad_along_width // 2
    pad_right = pad_along_width - pad_left
    padding = pad_left, pad_right, pad_top, pad_bottom
    output = out_height, out_width
    return padding, output