def find_unconserved_metabolites(model):
    problem = model.problem
    stoich_trans = problem.Model()
    internal_rxns = con_helpers.get_internals(model)
    metabolites = set(met for rxn in internal_rxns for met in rxn.metabolites)
    k_vars = list()
    for met in metabolites:
        m_var = problem.Variable(met.id)
        k_var = problem.Variable('k_{}'.format(met.id), type='binary')
        k_vars.append(k_var)
        stoich_trans.add([m_var, k_var])
        stoich_trans.add(problem.Constraint(k_var - m_var, ub=0, name=
            'switch_{}'.format(met.id)))
    stoich_trans.update()
    con_helpers.add_reaction_constraints(stoich_trans, internal_rxns,
        problem.Constraint)
    stoich_trans.objective = problem.Objective(Zero, sloppy=True, direction
        ='max')
    stoich_trans.objective.set_linear_coefficients({var: (1.0) for var in
        k_vars})
    status = stoich_trans.optimize()
    if status == OPTIMAL:
        return set([model.metabolites.get_by_id(var.name[2:]) for var in
            k_vars if var.primal < 0.8])
    else:
        raise RuntimeError(
            "Could not compute list of unconserved metabolites. Solver status is '{}' (only optimal expected)."
            .format(status))