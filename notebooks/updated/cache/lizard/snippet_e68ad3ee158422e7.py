def xmoe_tr_2d():
    hparams = xmoe_tr_dense_2k()
    hparams.mesh_shape = 'b0:2;b1:4'
    hparams.outer_batch_size = 4
    hparams.layout = 'outer_batch:b0;inner_batch:b1,expert_x:b1,expert_y:b0'
    hparams.encoder_layers = ['self_att', 'moe_2d'] * 4
    hparams.decoder_layers = ['self_att', 'enc_att', 'moe_2d'] * 4
    hparams.moe_hidden_size = 2048
    hparams.moe_experts_x = 4
    hparams.moe_experts_y = 4
    return hparams