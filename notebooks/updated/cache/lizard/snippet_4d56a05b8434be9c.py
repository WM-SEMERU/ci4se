def _join(self, node):
    select_block = str(node.attributes)
    from_block = '{left} {operator} {right}'.format(left=self._join_helper(
        node.left), right=self._join_helper(node.right), operator=self.
        _get_sql_operator(node))
    if node.operator == Operator.theta_join:
        from_block = '{from_block} ON {conditions}'.format(from_block=
            from_block, conditions=node.conditions)
    return self.query(select_block, from_block, '')