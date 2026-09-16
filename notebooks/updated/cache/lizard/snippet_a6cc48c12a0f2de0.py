def inference(images, num_classes, for_training=False, restore_logits=True,
    scope=None):
    batch_norm_params = {'decay': BATCHNORM_MOVING_AVERAGE_DECAY, 'epsilon':
        0.001}
    with slim.arg_scope([slim.ops.conv2d, slim.ops.fc], weight_decay=4e-05):
        with slim.arg_scope([slim.ops.conv2d], stddev=0.1, activation=tf.nn
            .relu, batch_norm_params=batch_norm_params):
            logits, endpoints = slim.inception.inception_v3(images,
                dropout_keep_prob=0.8, num_classes=num_classes, is_training
                =for_training, restore_logits=restore_logits, scope=scope)
    _activation_summaries(endpoints)
    auxiliary_logits = endpoints['aux_logits']
    return logits, auxiliary_logits