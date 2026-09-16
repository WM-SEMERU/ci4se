def explain(self, expr, params=None):
    if isinstance(expr, ir.Expr):
        context = self.dialect.make_context(params=params)
        query_ast = self._build_ast(expr, context)
        if len(query_ast.queries) > 1:
            raise Exception('Multi-query expression')
        query = query_ast.queries[0].compile()
    else:
        query = expr
    statement = 'EXPLAIN {0}'.format(query)
    with self._execute(statement, results=True) as cur:
        result = self._get_list(cur)
    return 'Query:\n{0}\n\n{1}'.format(util.indent(query, 2), '\n'.join(result)
        )