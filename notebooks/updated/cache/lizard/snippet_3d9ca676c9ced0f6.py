def attention_lm_moe_small():
    hparams = attention_lm_moe_base()
    hparams.num_hidden_layers = 4
    hparams.hidden_size = 512
    hparams.filter_size = 2048
    hparams.moe_num_experts = 128
    hparams.moe_layers = '2'
    return hparams