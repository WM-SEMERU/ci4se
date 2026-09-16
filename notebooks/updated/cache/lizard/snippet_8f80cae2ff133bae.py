def kl_with_logits(p_logits, q_logits, scope=None, loss_collection=tf.
    GraphKeys.REGULARIZATION_LOSSES):
    with tf.name_scope(scope, 'kl_divergence') as name:
        p = tf.nn.softmax(p_logits)
        p_log = tf.nn.log_softmax(p_logits)
        q_log = tf.nn.log_softmax(q_logits)
        loss = reduce_mean(reduce_sum(p * (p_log - q_log), axis=1), name=name)
        tf.losses.add_loss(loss, loss_collection)
        return loss