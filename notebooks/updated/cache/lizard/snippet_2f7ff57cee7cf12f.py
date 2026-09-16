def count_tokens_from_str(source_str, token_delim=' ', seq_delim='\n',
    to_lower=False, counter_to_update=None):
    source_str = filter(None, re.split(token_delim + '|' + seq_delim,
        source_str))
    if to_lower:
        source_str = [t.lower() for t in source_str]
    if counter_to_update is None:
        return collections.Counter(source_str)
    else:
        counter_to_update.update(source_str)
        return counter_to_update