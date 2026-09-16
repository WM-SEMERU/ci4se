def _evaluate_rhs(cls, funcs, nodes, problem):
    evald_funcs = cls._evaluate_functions(funcs, nodes)
    evald_rhs = problem.rhs(nodes, *evald_funcs, **problem.params)
    return evald_rhs