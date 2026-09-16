def find_metabolites_not_consumed_with_open_bounds(model):
    mets_not_consumed = list()
    helpers.open_exchanges(model)
    for met in model.metabolites:
        with model:
            exch = model.add_boundary(met, type='irrex', reaction_id=
                'IRREX', lb=-1000, ub=0)
            solution = helpers.run_fba(model, exch.id, direction='min')
            if np.isnan(solution) or abs(solution) < TOLERANCE_THRESHOLD:
                mets_not_consumed.append(met)
    return mets_not_consumed