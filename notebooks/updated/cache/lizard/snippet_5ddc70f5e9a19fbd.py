def compute_uncertainty_reward(logits, predictions):
    vocab_size = logits.shape[-1]
    assert vocab_size > 1
    log_probs = common_layers.log_prob_from_logits(logits)
    max_log_probs = common_layers.index_last_dim_with_indices(log_probs,
        predictions)
    neg_log_prob = tf.nn.relu(-max_log_probs - 0.02)
    reduce_dims = list(range(len(neg_log_prob.shape)))[1:]
    summed = tf.reduce_sum(neg_log_prob, axis=reduce_dims)
    return summed / 10