def mtf_transformer_paper_tr(size):
    n = 2 ** size
    hparams = mtf_transformer_base()
    hparams.label_smoothing = 0.1
    hparams.batch_size = 128
    hparams.d_model = 1024
    hparams.d_ff = int(4096 * n)
    hparams.num_heads = int(8 * n)
    hparams.shared_embedding_and_softmax_weights = False
    hparams.learning_rate_decay_steps = 51400
    return hparams