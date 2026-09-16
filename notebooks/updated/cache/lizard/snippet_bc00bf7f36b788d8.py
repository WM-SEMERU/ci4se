def create_model(name, *attributes, **params):
    params['register'] = False
    params['attributes'] = attributes
    kwargs = {'manager_class': params.pop('manager_class', Manager), 'Meta':
        params}
    return ModelType(name, (StdModel,), kwargs)