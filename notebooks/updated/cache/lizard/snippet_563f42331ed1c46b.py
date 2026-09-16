def visit_UnaryOp(self, node):
    if isinstance(node.op, Not):
        self._debug('UnaryOp', node.op, incr=1)
        operand = self[node.operand]
        self._debug('|-', operand, incr=2)
        tn = self._tn()
        result = numpy.logical_not(operand)
        self._debug('|_', result, incr=2)
        self[tn] = result
        return ast_name(tn)
    else:
        return self.generic_visit(node)