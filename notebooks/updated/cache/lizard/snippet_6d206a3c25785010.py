def batch_norm(self, input_layer=None, decay=0.999, scale=False, epsilon=0.001
    ):
    if input_layer is None:
        input_layer = self.top_layer
    else:
        self.top_size = None
    name = 'batchnorm' + str(self.counts['batchnorm'])
    self.counts['batchnorm'] += 1
    with tf.variable_scope(name) as scope:
        if self.use_tf_layers:
            bn = tf.contrib.layers.batch_norm(input_layer, decay=decay,
                scale=scale, epsilon=epsilon, is_training=self.phase_train,
                fused=True, data_format=self.data_format, scope=scope)
        else:
            bn = self._batch_norm_without_layers(input_layer, decay, scale,
                epsilon)
    self.top_layer = bn
    self.top_size = bn.shape[3] if self.data_format == 'NHWC' else bn.shape[1]
    self.top_size = int(self.top_size)
    return bn