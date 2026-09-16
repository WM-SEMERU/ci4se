def infix(tokens, operator_table):
    operator, matched_tokens = operator_table.infix.match(tokens)
    if operator:
        return TokenMatch(operator, None, matched_tokens)