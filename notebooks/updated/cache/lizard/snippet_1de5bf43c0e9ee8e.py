def get_data(model, instance_id, kind=''):
    instance = get_instance(model, instance_id)
    if not instance:
        return
    return ins2dict(instance, kind)