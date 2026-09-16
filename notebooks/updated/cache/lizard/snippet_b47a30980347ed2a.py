def register_model_once(cls, ModelClass, **kwargs):
    if cls._static_registry.get_for_model(ModelClass) is None:
        logger.warn("Model is already registered with {0}: '{1}'".format(
            cls, ModelClass))
    else:
        cls.register_model.register(ModelClass, **kwargs)