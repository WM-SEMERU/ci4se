def get_first_model_with_resource_name(cls, resource_name):
    models = cls.get_models_with_resource_name(resource_name)
    if len(models) > 0:
        return models[0]
    return None