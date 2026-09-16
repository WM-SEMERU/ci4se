def parse(infix):
    tokens = infix.replace('(', ' ( ').replace(')', ' ) ').strip().split()
    ops = deque()
    expressions = deque()
    for token in tokens:
        if token in TOKEN_ASSOCS:
            while len(ops) > 0 and ops[-1] in TOKEN_ASSOCS and (
                TOKEN_ASSOCS[token] == ASSOC_LEFT and TOKEN_PRECS[token] <=
                TOKEN_PRECS[ops[-1]] or TOKEN_ASSOCS[token] == ASSOC_RIGHT and
                TOKEN_PRECS[token] < TOKEN_PRECS[ops[-1]]):
                create_and_push_expression(ops.pop(), expressions)
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while len(ops) > 0 and ops[-1] != '(':
                create_and_push_expression(ops.pop(), expressions)
            if len(ops) == 0:
                raise TagExpressionError('Unclosed (')
            if ops[-1] == '(':
                ops.pop()
        else:
            create_and_push_expression(token, expressions)
    while len(ops) > 0:
        if ops[-1] == '(':
            raise TagExpressionError('Unclosed )')
        create_and_push_expression(ops.pop(), expressions)
    expression = expressions.pop()
    if len(expressions) > 0:
        raise TagExpressionError('Not empty')
    return expression