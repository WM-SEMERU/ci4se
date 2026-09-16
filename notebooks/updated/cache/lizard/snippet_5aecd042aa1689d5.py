def find_interchange_biomass_reactions(model, biomass=None):
    boundary = set(model.boundary)
    transporters = find_transport_reactions(model)
    if biomass is None:
        biomass = set(find_biomass_reaction(model))
    return boundary | transporters | biomass