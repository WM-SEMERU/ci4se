def find_biomass_precursors(model, reaction):
    id_of_main_compartment = helpers.find_compartment_id_in_model(model, 'c')
    gam_reactants = set()
    try:
        gam_reactants.update([helpers.find_met_in_model(model, 'MNXM3',
            id_of_main_compartment)[0]])
    except RuntimeError:
        pass
    try:
        gam_reactants.update([helpers.find_met_in_model(model, 'MNXM2',
            id_of_main_compartment)[0]])
    except RuntimeError:
        pass
    biomass_precursors = set(reaction.reactants) - gam_reactants
    return list(biomass_precursors)