def parse_objective_coefficient(entry):
    for parameter in entry.kinetic_law_reaction_parameters:
        pid, name, value, units = parameter
        if pid == 'OBJECTIVE_COEFFICIENT' or name == 'OBJECTIVE_COEFFICIENT':
            return value
    return None