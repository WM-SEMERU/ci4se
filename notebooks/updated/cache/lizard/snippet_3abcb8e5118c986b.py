def local_attention1d_spatial_decoder(x, kv_dim, heads_dim, feedforward_dim,
    hparams):
    batch_dim, length_dim, model_dim = x.shape.dims
    blocks_w_dim = mtf.Dimension('blocksw', hparams.block_length)
    num_w_blocks_dim = mtf.Dimension('num_wblocks', length_dim.size //
        blocks_w_dim.size)
    x = mtf.reshape(x, mtf.Shape([batch_dim, num_w_blocks_dim, blocks_w_dim,
        model_dim]))
    for layer in range(hparams.num_decoder_layers):
        layer_name = 'decoder_layer_%d' % layer
        with tf.variable_scope(layer_name):
            x += layer_prepostprocess_dropout(mtf.layers.
                local_self_attention_spatial_blocks(mtf.layers.layer_norm(x,
                model_dim, name='layer_norm_att'), kv_dim, heads_dim,
                memory_w_dim=blocks_w_dim, mask_right=True, name='self_att'
                ), hparams)
            x += layer_prepostprocess_dropout(mtf.layers.dense_relu_dense(
                mtf.layers.layer_norm(x, model_dim, name='layer_norm_ffn'),
                feedforward_dim, hparams.dropout, dropout_broadcast_dims=[
                length_dim]), hparams)
    output = mtf.layers.layer_norm(x, model_dim, name='final_layer_norm')
    return output