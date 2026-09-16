def rank_loss(sentence_emb, image_emb, margin=0.2):
    with tf.name_scope('rank_loss'):
        sentence_emb = tf.nn.l2_normalize(sentence_emb, 1)
        image_emb = tf.nn.l2_normalize(image_emb, 1)
        scores = tf.matmul(image_emb, tf.transpose(sentence_emb))
        diagonal = tf.diag_part(scores)
        cost_s = tf.maximum(0.0, margin - diagonal + scores)
        cost_im = tf.maximum(0.0, margin - tf.reshape(diagonal, [-1, 1]) +
            scores)
        batch_size = tf.shape(sentence_emb)[0]
        empty_diagonal_mat = tf.ones_like(cost_s) - tf.eye(batch_size)
        cost_s *= empty_diagonal_mat
        cost_im *= empty_diagonal_mat
        return tf.reduce_mean(cost_s) + tf.reduce_mean(cost_im)