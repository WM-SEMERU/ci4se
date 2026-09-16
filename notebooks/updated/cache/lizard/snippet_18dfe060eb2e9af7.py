def post_save_event_listener(sender, instance, created):
    if not instance._meta.event_ready:
        return
    if created:
        instance.create_creation_event()
    else:
        instance.create_update_event()
    instance._original = None