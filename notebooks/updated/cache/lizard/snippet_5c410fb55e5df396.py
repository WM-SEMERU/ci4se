def shake_shake_skip_connection(x, output_filters, stride, is_training):
    curr_filters = common_layers.shape_list(x)[-1]
    if curr_filters == output_filters:
        return x
    stride_spec = [1, stride, stride, 1]
    path1 = tf.nn.avg_pool(x, [1, 1, 1, 1], stride_spec, 'VALID')
    path1 = tf.layers.conv2d(path1, int(output_filters / 2), (1, 1),
        padding='SAME', name='path1_conv')
    pad_arr = [[0, 0], [0, 1], [0, 1], [0, 0]]
    path2 = tf.pad(x, pad_arr)[:, 1:, 1:, :]
    path2 = tf.nn.avg_pool(path2, [1, 1, 1, 1], stride_spec, 'VALID')
    path2 = tf.layers.conv2d(path2, int(output_filters / 2), (1, 1),
        padding='SAME', name='path2_conv')
    final_path = tf.concat(values=[path1, path2], axis=-1)
    final_path = tf.layers.batch_normalization(final_path, training=
        is_training, name='final_path_bn')
    return final_path