def build_traversal(self, traversal):
    rhs_label = ':' + traversal.target_class.__label__
    lhs_ident = self.build_source(traversal.source)
    rhs_ident = traversal.name + rhs_label
    self._ast['return'] = traversal.name
    self._ast['result_class'] = traversal.target_class
    rel_ident = self.create_ident()
    stmt = _rel_helper(lhs=lhs_ident, rhs=rhs_ident, ident=rel_ident, **
        traversal.definition)
    self._ast['match'].append(stmt)
    if traversal.filters:
        self.build_where_stmt(rel_ident, traversal.filters)
    return traversal.name