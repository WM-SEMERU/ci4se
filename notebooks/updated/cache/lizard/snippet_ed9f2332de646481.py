def optimize(objective_function, domain, stopping_condition, parameters=
    None, position_update=functions.std_position, velocity_update=functions
    .std_velocity, parameter_update=functions.std_parameter_update,
    measurements=(), measurer=dictionary_based_metrics):
    params = __init_parameters__(parameters)
    rng = np.random.RandomState(params['seed'])
    initial_swarm = [functions.initialize_particle(rng, domain,
        objective_function) for i in range(params['swarm_size'])]
    state = types.PSOState(rng, params, iterations=0, swarm=initial_swarm)
    topology_function = state.params['topology']
    update_fitness = functions.update_fitness
    update_particle = functions.update_particle
    results, measure = measurer(measurements)
    while not stopping_condition(state):
        n_bests = topology_function(state)
        state = state._replace(swarm=[update_particle(position_update,
            velocity_update, state, n_bests, ip) for ip in enumerate(state.
            swarm)])
        state = state._replace(swarm=[update_fitness(objective_function,
            particle) for particle in state.swarm], iterations=state.
            iterations + 1)
        state = parameter_update(state, objective_function)
        results = measure(results, state)
    return functions.solution(state.swarm), results