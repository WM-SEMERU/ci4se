def delete(self, *args, **kwargs):
    from bakery import tasks
    from django.contrib.contenttypes.models import ContentType
    unpublish = kwargs.pop('unpublish', True)
    super(AutoPublishingBuildableModel, self).delete(*args, **kwargs)
    if unpublish:
        ct = ContentType.objects.get_for_model(self.__class__)
        tasks.unpublish_object.delay(ct.pk, self.pk)