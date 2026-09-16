def eval_expression(self, t):
    t = CPP_to_Python(' '.join(t[1:]))
    try:
        return eval(t, self.cpp_namespace)
    except (NameError, TypeError):
        return 0