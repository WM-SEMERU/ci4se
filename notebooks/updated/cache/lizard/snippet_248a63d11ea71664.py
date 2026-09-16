def app_model_id(obj):
    ct = ContentType.objects.get_for_model(obj)
    return '%s-%s-%s' % (ct.app_label, ct.model, obj.id)