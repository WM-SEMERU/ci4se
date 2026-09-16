def _related_items_changed(self, **kwargs):
    for_model = kwargs['instance'].content_type.model_class()
    if for_model and issubclass(for_model, self.model):
        instance_id = kwargs['instance'].object_pk
        try:
            instance = for_model.objects.get(id=instance_id)
        except self.model.DoesNotExist:
            return
        if hasattr(instance, 'get_content_model'):
            instance = instance.get_content_model()
        related_manager = getattr(instance, self.related_field_name)
        self.related_items_changed(instance, related_manager)