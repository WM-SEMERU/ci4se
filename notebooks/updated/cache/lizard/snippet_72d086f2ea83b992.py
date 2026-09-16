def get_drake_data(steps):
    output_inputs = {}
    if len(steps) == 0:
        return output_inputs
    for step in steps:
        output_inputs[step] = get_inputs(step, target=True)
    inputs = set(itertools.chain(*output_inputs.values()))
    o = get_drake_data(inputs)
    output_inputs.update(o)
    return output_inputs