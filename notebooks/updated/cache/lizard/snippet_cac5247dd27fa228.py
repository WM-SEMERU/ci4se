def compute_qkv(query_antecedent, memory_antecedent, total_key_depth,
    total_value_depth, q_filter_width=1, kv_filter_width=1, q_padding=
    'VALID', kv_padding='VALID', vars_3d_num_heads=0, layer_collection=None):
    if memory_antecedent is None:
        memory_antecedent = query_antecedent
    q = compute_attention_component(query_antecedent, total_key_depth,
        q_filter_width, q_padding, 'q', vars_3d_num_heads=vars_3d_num_heads,
        layer_collection=layer_collection)
    k = compute_attention_component(memory_antecedent, total_key_depth,
        kv_filter_width, kv_padding, 'k', vars_3d_num_heads=
        vars_3d_num_heads, layer_collection=layer_collection)
    v = compute_attention_component(memory_antecedent, total_value_depth,
        kv_filter_width, kv_padding, 'v', vars_3d_num_heads=
        vars_3d_num_heads, layer_collection=layer_collection)
    return q, k, v