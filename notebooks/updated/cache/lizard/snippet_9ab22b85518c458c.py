def set_literal_handle(self, tokens):
    internal_assert(len(tokens) == 1 and len(tokens[0]) == 1,
        'invalid set literal tokens', tokens)
    if self.target_info < (2, 7):
        return '_coconut.set(' + set_to_tuple(tokens[0]) + ')'
    else:
        return '{' + tokens[0][0] + '}'