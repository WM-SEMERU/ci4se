def post_migrate(cls, sender=None, **kwargs):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    for model_name, proxy_model in sender.get_proxy_models().items():
        ctype, created = ContentType.objects.get_or_create(app_label=sender
            .label, model=model_name)
        if created:
            sender.grant_permissions(proxy_model)