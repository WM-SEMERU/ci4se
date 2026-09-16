def filter_pipeline(effects, filters):
    for filter_fn in filters:
        filtered_effects = filter_fn(effects)
        if len(effects) == 1:
            return effects
        elif len(filtered_effects) > 1:
            effects = filtered_effects
    return effects