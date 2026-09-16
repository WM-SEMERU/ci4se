def is_reduction(expr):

    def has_reduction(op):
        if getattr(op, '_reduction', False):
            return True
        for arg in op.args:
            if isinstance(arg, ir.ScalarExpr) and has_reduction(arg.op()):
                return True
        return False
    return has_reduction(expr.op() if isinstance(expr, ir.Expr) else expr)