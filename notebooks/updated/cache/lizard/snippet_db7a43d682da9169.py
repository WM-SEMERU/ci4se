def get_model_name(model):
    opts = model._meta
    if django.VERSION[:2] < (1, 7):
        model_name = opts.module_name
    else:
        model_name = opts.model_name
    return model_name