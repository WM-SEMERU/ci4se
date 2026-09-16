def _delete(self, tree):
    tablename = tree.table
    table = self.describe(tablename, require=True)
    kwargs = {}
    visitor = Visitor(self.reserved_words)
    if tree.where:
        constraints = ConstraintExpression.from_where(tree.where)
        kwargs['condition'] = constraints.build(visitor)
    kwargs['expr_values'] = visitor.expression_values
    kwargs['alias'] = visitor.attribute_names
    return self._query_and_op(tree, table, 'delete_item', kwargs)