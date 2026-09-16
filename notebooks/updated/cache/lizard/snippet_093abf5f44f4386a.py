def set_defaults(self, config, fields_spec):
    defaults = dict([(f, d) for f, d in fields_spec.items() if not
        isinstance(d, type)])
    for field, default_value in defaults.items():
        if field not in config:
            config[field] = default_value