def make_tree(statement, filename='<aexec>', symbol='single', local={}):
    tree = ast.parse(CORO_CODE, filename, symbol)
    if isinstance(statement, ast.Expr):
        tree.body[0].body[0].value.elts[0] = statement.value
    else:
        tree.body[0].body.insert(0, statement)
    exec(compile(tree, filename, symbol))
    return tree