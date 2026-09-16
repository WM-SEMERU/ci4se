def soma_surface_areas(nrn_pop, neurite_type=NeuriteType.soma):
    nrns = neuron_population(nrn_pop)
    assert neurite_type == NeuriteType.soma, 'Neurite type must be soma'
    return [soma_surface_area(n) for n in nrns]