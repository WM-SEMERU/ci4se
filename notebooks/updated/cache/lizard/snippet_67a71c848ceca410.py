def detect_extracellular_compartment(model):
    extracellular_key = Counter()
    for reaction in model.reactions:
        equation = reaction.equation
        if equation is None:
            continue
        if len(equation.compounds) == 1:
            compound, _ = equation.compounds[0]
            compartment = compound.compartment
            extracellular_key[compartment] += 1
    if len(extracellular_key) == 0:
        return None
    else:
        best_key, _ = extracellular_key.most_common(1)[0]
    logger.info('{} is extracellular compartment'.format(best_key))
    return best_key