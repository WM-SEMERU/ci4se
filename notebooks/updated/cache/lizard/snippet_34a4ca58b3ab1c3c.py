def issue_post_delete(instance, *args, **kwargs):
    LOGGER.debug('Re-adding layer/service to search engine index')
    if isinstance(instance.content_object, Service):
        if not settings.REGISTRY_SKIP_CELERY:
            index_service.delay(instance.content_object.id)
        else:
            index_service(instance.content_object.id)
    elif not settings.REGISTRY_SKIP_CELERY:
        index_layer.delay(instance.content_object.id)
    else:
        index_layer(instance.content_object.id)