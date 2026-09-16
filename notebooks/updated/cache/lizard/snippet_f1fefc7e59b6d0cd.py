def on_compare(self, node):
    lval = self.run(node.left)
    out = True
    for op, rnode in zip(node.ops, node.comparators):
        rval = self.run(rnode)
        out = op2func(op)(lval, rval)
        lval = rval
        if self.use_numpy and isinstance(out, numpy.ndarray) and out.any():
            break
        elif not out:
            break
    return out