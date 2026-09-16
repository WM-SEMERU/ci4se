def simplify_scalar(self, func=sympy.simplify):

    def element_simplify(v):
        if isinstance(v, sympy.Basic):
            return func(v)
        elif isinstance(v, QuantumExpression):
            return v.simplify_scalar(func=func)
        else:
            return v
    return self.element_wise(element_simplify)