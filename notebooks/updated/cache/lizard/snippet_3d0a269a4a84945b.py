def _create_update_tracking_event(instance):
    event = _create_event(instance, UPDATE)
    for field in instance._tracked_fields:
        if not isinstance(instance._meta.get_field(field), ManyToManyField):
            try:
                if isinstance(instance._meta.get_field(field), ForeignKey):
                    value = getattr(instance, '{0}_id'.format(field))
                else:
                    value = getattr(instance, field)
                if instance._original_fields[field] != value:
                    _create_tracked_field(event, instance, field)
            except TypeError:
                _create_tracked_field(event, instance, field)