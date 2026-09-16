def get_original_before_save(sender, instance, created):
    if not instance._meta.event_ready or created:
        return
    instance.get_original()