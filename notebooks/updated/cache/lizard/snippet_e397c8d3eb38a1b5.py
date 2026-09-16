def essential_precursors_not_in_biomass(model, reaction):
    u
    main_comp = helpers.find_compartment_id_in_model(model, 'c')
    biomass_eq = bundle_biomass_components(model, reaction)
    pooled_precursors = set([met for rxn in biomass_eq for met in rxn.
        metabolites])
    missing_essential_precursors = []
    for mnx_id in ESSENTIAL_PRECURSOR_IDS:
        try:
            met = helpers.find_met_in_model(model, mnx_id, main_comp)[0]
            if met not in pooled_precursors:
                missing_essential_precursors.append(met.id)
        except RuntimeError:
            missing_essential_precursors.append(mnx_id)
    return missing_essential_precursors