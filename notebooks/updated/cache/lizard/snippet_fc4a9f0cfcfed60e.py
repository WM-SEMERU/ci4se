def discriminator(self, frames):
    ndf = self.hparams.num_discriminator_filters
    frames = tf.stack(frames)
    frames = common_video.swap_time_and_batch_axes(frames)
    num_outputs = [ndf, ndf * 2, ndf * 2, ndf * 4, ndf * 4, ndf * 8, ndf * 8]
    kernel_sizes = [3, 4, 3, 4, 3, 4, 3]
    strides = [[1, 1, 1], [1, 2, 2], [1, 1, 1], [1, 2, 2], [1, 1, 1], [2, 2,
        2], [1, 1, 1]]
    names = ['video_sn_conv0_0', 'video_sn_conv0_1', 'video_sn_conv1_0',
        'video_sn_conv1_1', 'video_sn_conv2_0', 'video_sn_conv2_1',
        'video_sn_conv3_0']
    iterable = zip(num_outputs, kernel_sizes, strides, names)
    activations = frames
    for num_filters, kernel_size, stride, name in iterable:
        activations = self.pad_conv3d_lrelu(activations, num_filters,
            kernel_size, stride, name)
    num_fc_dimensions = self.get_fc_dimensions(strides, kernel_sizes)
    activations = tf.reshape(activations, (-1, num_fc_dimensions))
    return tf.squeeze(tf.layers.dense(activations, 1))