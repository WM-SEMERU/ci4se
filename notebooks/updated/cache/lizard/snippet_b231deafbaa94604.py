def rtype_to_model(rtype):
    models = goldman.config.MODELS
    for model in models:
        if rtype.lower() == model.RTYPE.lower():
            return model
    raise ValueError('%s resource type not registered' % rtype)