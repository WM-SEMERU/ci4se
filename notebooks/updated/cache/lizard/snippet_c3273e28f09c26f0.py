def attention_params_simple(mesh, io_dim, kv_dim, heads_dim, variable_dtype):
    return AttentionParams(mesh, query_input_dim=io_dim, memory_input_dim=
        io_dim, output_dim=io_dim, key_dim=kv_dim, value_dim=kv_dim,
        query_heads_dims=[heads_dim], memory_heads_dims=[heads_dim],
        variable_dtype=variable_dtype)