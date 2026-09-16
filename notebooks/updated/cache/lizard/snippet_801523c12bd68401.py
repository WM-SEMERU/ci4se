def resolve_expression(self, query=None, allow_joins=True, reuse=None,
    summarize=False, for_save=False):
    c = self.copy()
    c.is_summary = summarize
    c.for_save = for_save
    for pos, expression in enumerate(self.expressions):
        c.expressions[pos] = expression.resolve_expression(query,
            allow_joins, reuse, summarize)
    return c