def embedding_to_padding(emb):
    emb_sum = tf.reduce_sum(tf.abs(emb), axis=-1, keep_dims=True)
    return tf.to_float(tf.equal(emb_sum, 0.0))