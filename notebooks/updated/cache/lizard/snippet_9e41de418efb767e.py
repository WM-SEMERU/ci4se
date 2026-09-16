def _get_types_from_sample(result_vars, sparql_results_json):
    total_bindings = len(sparql_results_json['results']['bindings'])
    homogeneous_types = {}
    for result_var in result_vars:
        var_types = set()
        var_datatypes = set()
        for i in range(0, min(total_bindings, 10)):
            binding = sparql_results_json['results']['bindings'][i]
            rdf_term = binding.get(result_var)
            if rdf_term is not None:
                var_types.add(rdf_term.get('type'))
                var_datatypes.add(rdf_term.get('datatype'))
        if len(var_types) > 1 or len(var_datatypes) > 1:
            return None
        else:
            homogeneous_types[result_var] = {'type': var_types.pop() if
                var_types else None, 'datatype': var_datatypes.pop() if
                var_datatypes else None}
    return homogeneous_types