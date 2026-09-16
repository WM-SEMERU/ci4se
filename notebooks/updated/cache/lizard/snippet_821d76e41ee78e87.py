def to_projection(self):
    roots = self._root_tables()
    if len(roots) > 1:
        raise com.RelationError(
            'Cannot convert array expression involving multiple base table references to a projection'
            )
    table = TableExpr(roots[0])
    return table.projection([self])