def models_of_config(config):
    resources = resources_of_config(config)
    models = []
    for resource in resources:
        if not hasattr(resource, '__table__') and hasattr(resource, 'model'):
            models.append(resource.model)
        else:
            models.append(resource)
    return models