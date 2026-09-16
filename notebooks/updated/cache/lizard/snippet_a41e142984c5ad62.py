def universal_transformer_base_range(rhp):
    rhp.set_discrete('num_rec_steps', [6, 8, 10])
    rhp.set_discrete('hidden_size', [1024, 2048, 4096])
    rhp.set_discrete('filter_size', [2048, 4096, 8192])
    rhp.set_discrete('num_heads', [8, 16, 32])
    rhp.set_discrete('transformer_ffn_type', ['sepconv', 'fc'])
    rhp.set_float('learning_rate', 0.3, 3.0, scale=rhp.LOG_SCALE)
    rhp.set_float('weight_decay', 0.0, 2.0)