def slice_hidden(x, hidden_size, num_blocks):
    batch_size, latent_dim, _ = common_layers.shape_list(x)
    block_dim = hidden_size // num_blocks
    x_sliced = tf.reshape(x, shape=[batch_size, latent_dim, num_blocks,
        block_dim])
    return x_sliced