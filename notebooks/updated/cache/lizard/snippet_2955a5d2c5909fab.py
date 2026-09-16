def visit_binop(self, node):
    left = self._precedence_parens(node, node.left)
    right = self._precedence_parens(node, node.right, is_left=False)
    if node.op == '**':
        return '%s%s%s' % (left, node.op, right)
    return '%s %s %s' % (left, node.op, right)