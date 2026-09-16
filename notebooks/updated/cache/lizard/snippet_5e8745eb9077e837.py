def _get_django_objects(model):
    model_name = model.__class__.__name__
    model_objects = [i for i in model.objects.all()]
    logger.debug('Found {} {} objects in DB'.format(len(model_objects),
        model_name))
    return model_objects