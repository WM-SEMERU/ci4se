def cdna_transformation(prev_image, cdna_input, num_masks, color_channels,
    dna_kernel_size, relu_shift):
    batch_size = tf.shape(cdna_input)[0]
    height = int(prev_image.get_shape()[1])
    width = int(prev_image.get_shape()[2])
    cdna_kerns = tfl.dense(cdna_input, dna_kernel_size * dna_kernel_size *
        num_masks, name='cdna_params', activation=None)
    cdna_kerns = tf.reshape(cdna_kerns, [batch_size, dna_kernel_size,
        dna_kernel_size, 1, num_masks])
    cdna_kerns = tf.nn.relu(cdna_kerns - relu_shift) + relu_shift
    norm_factor = tf.reduce_sum(cdna_kerns, [1, 2, 3], keep_dims=True)
    cdna_kerns /= norm_factor
    cdna_kerns = tf.transpose(cdna_kerns, [1, 2, 0, 4, 3])
    cdna_kerns = tf.reshape(cdna_kerns, [dna_kernel_size, dna_kernel_size,
        batch_size, num_masks])
    prev_image = tf.transpose(prev_image, [3, 1, 2, 0])
    transformed = tf.nn.depthwise_conv2d(prev_image, cdna_kerns, [1, 1, 1, 
        1], 'SAME')
    transformed = tf.reshape(transformed, [color_channels, height, width,
        batch_size, num_masks])
    transformed = tf.transpose(transformed, [3, 1, 2, 0, 4])
    transformed = tf.unstack(transformed, axis=-1)
    return transformed