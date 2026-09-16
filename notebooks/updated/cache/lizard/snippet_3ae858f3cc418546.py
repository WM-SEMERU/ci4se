def unembed_samples(samples, embedding, chain_break_method=None):
    if chain_break_method is None:
        chain_break_method = majority_vote
    return list(itertools.chain(*(chain_break_method(sample, embedding) for
        sample in samples)))