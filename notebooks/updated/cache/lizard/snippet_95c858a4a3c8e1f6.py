def mention_to_tokens(mention, token_type='words', lowercase=False):
    tokens = mention.context.sentence.__dict__[token_type]
    return [(w.lower() if lowercase else w) for w in tokens]