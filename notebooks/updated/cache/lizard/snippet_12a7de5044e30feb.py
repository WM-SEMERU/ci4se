def transformer_moe_prepend_8k():
    hparams = transformer_moe_8k()
    hparams.prepend_mode = 'prepend_inputs_masked_attention'
    hparams.eval_drop_long_sequences = False
    hparams.max_input_seq_length = 7500
    hparams.default_ff = 'sepm'
    hparams.layer_types = 'locm/redm/locm-moe/redm/locm'
    hparams.moe_num_experts = 256
    return hparams