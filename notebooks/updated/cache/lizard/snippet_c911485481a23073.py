def visit_BoolOp(self, node):
    res = list(zip(*[self.visit(elt).bounds() for elt in node.values]))
    return self.add(node, Interval(min(res[0]), max(res[1])))