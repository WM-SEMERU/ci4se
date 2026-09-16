def power_ngram(iter_tokens):
    return chain.from_iterable(ngram(j, iter_tokens) for j in range(1, len(
        iter_tokens) + 1))