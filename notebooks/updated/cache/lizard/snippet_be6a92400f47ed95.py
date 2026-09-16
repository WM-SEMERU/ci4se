def reduce_to_parent_states(models):
    models = set(models)
    models_to_remove = set()
    for model in models:
        parent_m = model.parent
        while parent_m is not None:
            if parent_m in models:
                models_to_remove.add(model)
                break
            parent_m = parent_m.parent
    for model in models_to_remove:
        models.remove(model)
    if models_to_remove:
        logger.debug(
            'The selection has been reduced, as it may not contain elements whose children are also selected'
            )
    return models