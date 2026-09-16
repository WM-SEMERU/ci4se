def _split_along_width(x_left_right_blocks):
    (_, x_num_h_blocks, x_num_outer_w_blocks, x_memory_flange_h,
        x_memory_flange_w, depth) = common_layers.shape_list(
        x_left_right_blocks)
    x_num_w_blocks = (x_num_outer_w_blocks - 1) // 2
    x_left_right_blocks = tf.reshape(x_left_right_blocks, [-1,
        x_num_h_blocks, x_num_outer_w_blocks // 2, 2, x_memory_flange_h,
        x_memory_flange_w, depth])
    x_left_blocks, x_right_blocks = tf.split(x_left_right_blocks,
        num_or_size_splits=2, axis=3)
    x_left_blocks = tf.squeeze(x_left_blocks, axis=3)
    x_right_blocks = tf.squeeze(x_right_blocks, axis=3)
    x_left_blocks = tf.slice(x_left_blocks, [0, 0, 0, 0, 0, 0], [-1, -1,
        x_num_w_blocks, -1, -1, -1])
    x_right_blocks = tf.slice(x_right_blocks, [0, 0, 1, 0, 0, 0], [-1, -1,
        x_num_w_blocks, -1, -1, -1])
    return x_left_blocks, x_right_blocks