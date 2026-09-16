def validate_experimental(context, param, value):
    if value is None:
        return
    config = ExperimentConfiguration(value)
    config.validate()
    return config