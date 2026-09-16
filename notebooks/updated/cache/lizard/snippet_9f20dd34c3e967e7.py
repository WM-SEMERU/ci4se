def nce_loss_subwords(data, label, label_mask, label_weight, embed_weight,
    vocab_size, num_hidden):
    label_units_embed = mx.sym.Embedding(data=label, input_dim=vocab_size,
        weight=embed_weight, output_dim=num_hidden)
    label_units_embed = mx.sym.broadcast_mul(lhs=label_units_embed, rhs=
        label_mask, name='label_units_embed')
    label_embed = mx.sym.sum(label_units_embed, axis=2, name='label_embed')
    data = mx.sym.Reshape(data=data, shape=(-1, 1, num_hidden))
    pred = mx.sym.broadcast_mul(data, label_embed)
    pred = mx.sym.sum(data=pred, axis=2)
    return mx.sym.LogisticRegressionOutput(data=pred, label=label_weight)