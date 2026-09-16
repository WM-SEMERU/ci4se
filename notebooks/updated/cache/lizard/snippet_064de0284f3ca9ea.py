def image_embedding(images, model_fn=resnet_v1_152, trainable=True,
    is_training=True, weight_decay=0.0001, batch_norm_decay=0.997,
    batch_norm_epsilon=1e-05, batch_norm_scale=True, add_summaries=False,
    reuse=False):
    is_resnet_training = trainable and is_training
    batch_norm_params = {'is_training': is_resnet_training, 'trainable':
        trainable, 'decay': batch_norm_decay, 'epsilon': batch_norm_epsilon,
        'scale': batch_norm_scale}
    if trainable:
        weights_regularizer = tf.contrib.layers.l2_regularizer(weight_decay)
    else:
        weights_regularizer = None
    with tf.variable_scope(model_fn.__name__, [images], reuse=reuse) as scope:
        with slim.arg_scope([slim.conv2d], weights_regularizer=
            weights_regularizer, trainable=trainable):
            with slim.arg_scope([slim.conv2d], weights_initializer=slim.
                variance_scaling_initializer(), activation_fn=tf.nn.relu,
                normalizer_fn=slim.batch_norm, normalizer_params=
                batch_norm_params):
                with slim.arg_scope([slim.batch_norm], is_training=
                    is_resnet_training, trainable=trainable):
                    with slim.arg_scope([slim.max_pool2d], padding='SAME'):
                        net, end_points = model_fn(images, num_classes=None,
                            global_pool=False, is_training=
                            is_resnet_training, reuse=reuse, scope=scope)
    if add_summaries:
        for v in end_points.values():
            tf.contrib.layers.summaries.summarize_activation(v)
    return net