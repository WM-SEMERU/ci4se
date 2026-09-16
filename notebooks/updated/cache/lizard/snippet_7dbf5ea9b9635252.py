def get_data_by_slug(model, slug, kind='', **kwargs):
    instance = get_instance_by_slug(model, slug, **kwargs)
    if not instance:
        return
    return ins2dict(instance, kind)