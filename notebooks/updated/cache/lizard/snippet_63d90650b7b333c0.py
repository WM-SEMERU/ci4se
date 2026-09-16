def map_query(self, variables=None, evidence=None, elimination_order=None):
    final_distribution = self._variable_elimination(variables,
        'marginalize', evidence=evidence, elimination_order=elimination_order)
    argmax = np.argmax(final_distribution.values)
    assignment = final_distribution.assignment([argmax])[0]
    map_query_results = {}
    for var_assignment in assignment:
        var, value = var_assignment
        map_query_results[var] = value
    if not variables:
        return map_query_results
    else:
        return_dict = {}
        for var in variables:
            return_dict[var] = map_query_results[var]
        return return_dict