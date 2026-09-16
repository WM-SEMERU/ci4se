def _count_and_gen_subtokens(token_counts, alphabet, subtoken_dict,
    max_subtoken_length):
    subtoken_counts = collections.defaultdict(int)
    for token, count in six.iteritems(token_counts):
        token = _escape_token(token, alphabet)
        subtokens = _split_token_to_subtokens(token, subtoken_dict,
            max_subtoken_length)
        start = 0
        for subtoken in subtokens:
            for end in xrange(start + 1, len(token) + 1):
                new_subtoken = token[start:end]
                subtoken_counts[new_subtoken] += count
            start += len(subtoken)
    return subtoken_counts