def highway_core_with_recurrent_dropout(hidden_size, num_layers, keep_prob=
    0.5, **kwargs):
    core = HighwayCore(hidden_size, num_layers, **kwargs)
    return RecurrentDropoutWrapper(core, keep_prob), core