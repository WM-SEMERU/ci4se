def _prepare_requirements(configs, requires_filters):
    if not requires_filters or not isinstance(requires_filters, dict):
        return configs
    new_requirements = {}
    for field, config in configs.items():
        requirement, key, allow_none = config
        try:
            explicit_filter = requires_filters[field]
            requirement_copy = requirement.copy()
            requirement_copy.set_filter(explicit_filter)
            new_requirements[field] = requirement_copy, key, allow_none
        except (KeyError, TypeError, ValueError):
            new_requirements[field] = config
    return new_requirements