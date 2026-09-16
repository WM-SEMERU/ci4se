def fitness_and_quality_parsed(mime_type, parsed_ranges):
    best_fitness = -1
    best_fit_q = 0
    target_type, target_subtype, target_params = parse_media_range(mime_type)
    for type, subtype, params in parsed_ranges:
        if (type == target_type or type == '*' or target_type == '*') and (
            subtype == target_subtype or subtype == '*' or target_subtype ==
            '*'):
            param_matches = reduce(lambda x, y: x + y, [(1) for key, value in
                list(target_params.items()) if key != 'q' and key in params and
                value == params[key]], 0)
            fitness = type == target_type and 100 or 0
            fitness += subtype == target_subtype and 10 or 0
            fitness += param_matches
            if fitness > best_fitness:
                best_fitness = fitness
                best_fit_q = params['q']
    return float(best_fit_q), best_fitness