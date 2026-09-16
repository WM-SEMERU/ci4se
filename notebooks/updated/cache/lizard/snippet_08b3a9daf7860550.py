def add_time_dimension(padded_inputs, seq_lens):
    padded_batch_size = tf.shape(padded_inputs)[0]
    max_seq_len = padded_batch_size // tf.shape(seq_lens)[0]
    new_batch_size = padded_batch_size // max_seq_len
    new_shape = [new_batch_size, max_seq_len] + padded_inputs.get_shape(
        ).as_list()[1:]
    return tf.reshape(padded_inputs, new_shape)