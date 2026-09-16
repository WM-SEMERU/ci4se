def padded_neg_log_perplexity(logits, labels, vocab_size):
    num, den = padded_cross_entropy_loss(logits, labels, 0, vocab_size)
    return -num, den