def _highest_degree_variable_chooser(problem, variables, domains):
    return sorted(variables, key=lambda v: problem.var_degrees[v], reverse=True
        )[0]