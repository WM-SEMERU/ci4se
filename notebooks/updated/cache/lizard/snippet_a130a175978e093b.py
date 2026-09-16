def mtr_tr_dense(sz):
    n = 2 ** sz
    hparams = mtf_bitransformer_base()
    hparams.d_model = 1024
    hparams.max_length = 256
    hparams.batch_size = 128
    hparams.d_ff = int(4096 * n)
    hparams.d_kv = 128
    hparams.encoder_num_heads = int(8 * n)
    hparams.decoder_num_heads = int(8 * n)
    hparams.learning_rate_decay_steps = 51400
    hparams.layout = 'batch:batch;vocab:model;d_ff:model;heads:model'
    hparams.mesh_shape = 'batch:32'
    hparams.label_smoothing = 0.1
    hparams.layer_prepostprocess_dropout = 0.1
    hparams.attention_dropout = 0.1
    hparams.relu_dropout = 0.1
    return hparams