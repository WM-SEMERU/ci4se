def _parse_container(tokens, index, for_or_if=None):
    items = [Atom(Token(*tokens[index]))]
    index += 1
    num_tokens = len(tokens)
    while index < num_tokens:
        tok = Token(*tokens[index])
        if tok.token_string in ',)]}':
            if for_or_if == 'for':
                return ListComprehension(items), index - 1
            elif for_or_if == 'if':
                return IfExpression(items), index - 1
            items.append(Atom(tok))
            if tok.token_string == ')':
                return Tuple(items), index
            elif tok.token_string == ']':
                return List(items), index
            elif tok.token_string == '}':
                return DictOrSet(items), index
        elif tok.token_string in '([{':
            container, index = _parse_container(tokens, index)
            items.append(container)
        elif tok.token_string == 'for':
            container, index = _parse_container(tokens, index, 'for')
            items.append(container)
        elif tok.token_string == 'if':
            container, index = _parse_container(tokens, index, 'if')
            items.append(container)
        else:
            items.append(Atom(tok))
        index += 1
    return None, None