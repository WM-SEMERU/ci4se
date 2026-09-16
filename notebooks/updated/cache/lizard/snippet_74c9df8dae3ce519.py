def has_metric_plateaued(steps, values, num_steps=100, delta=0.1, decrease=True
    ):
    assert num_steps > 0
    if len(steps) < 2:
        return False
    steps_at_least_num_steps_ago = [s for s in steps if s <= steps[-1] -
        num_steps]
    if not steps_at_least_num_steps_ago:
        return False
    delta_step_idx = len(steps_at_least_num_steps_ago) - 1
    start_val = values[delta_step_idx]
    values_to_check = values[delta_step_idx:]
    observed_deltas = []
    for val in values_to_check:
        if decrease:
            observed_delta = start_val - val
        else:
            observed_delta = val - start_val
        observed_deltas.append(observed_delta)
    within_range = [(obs < delta) for obs in observed_deltas]
    return all(within_range)