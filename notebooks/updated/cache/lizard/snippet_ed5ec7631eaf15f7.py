def apply_customizations(cls, spec, options):
    for key in sorted(spec.keys()):
        if isinstance(spec[key], (list, tuple)):
            customization = {v.key: v for v in spec[key]}
        else:
            customization = {k: (Options(**v) if isinstance(v, dict) else v
                ) for k, v in spec[key].items()}
        customization = {k: v.keywords_target(key.split('.')[0]) for k, v in
            customization.items()}
        options[str(key)] = customization
    return options