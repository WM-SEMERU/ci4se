def set_letter_literal_handle(self, tokens):
    if len(tokens) == 1:
        set_type = tokens[0]
        if set_type == 's':
            return '_coconut.set()'
        elif set_type == 'f':
            return '_coconut.frozenset()'
        else:
            raise CoconutInternalException('invalid set type', set_type)
    elif len(tokens) == 2:
        set_type, set_items = tokens
        internal_assert(len(set_items) == 1, 'invalid set literal item',
            tokens[0])
        if set_type == 's':
            return self.set_literal_handle([set_items])
        elif set_type == 'f':
            return '_coconut.frozenset(' + set_to_tuple(set_items) + ')'
        else:
            raise CoconutInternalException('invalid set type', set_type)
    else:
        raise CoconutInternalException('invalid set literal tokens', tokens)