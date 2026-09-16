def tokenize_fielded(self, tw):
    toks = self.tokenize(tw)
    for field, tokens in sorted(toks.items()):
        for tok in tokens:
            yield '%s___%s' % (field, tok)