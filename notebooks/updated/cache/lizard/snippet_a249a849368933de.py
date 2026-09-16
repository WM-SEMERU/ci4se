def apply_hyperparameter_renames(cls, hyperparameters):
    for from_name, to_name in cls.hyperparameter_renames.items():
        if from_name in hyperparameters:
            value = hyperparameters.pop(from_name)
            if to_name:
                hyperparameters[to_name] = value
    return hyperparameters