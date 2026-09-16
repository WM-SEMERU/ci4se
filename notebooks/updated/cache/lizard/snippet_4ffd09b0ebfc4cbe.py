def update_default_channels(sender, instance, created, **kwargs):
    if instance.default:
        Channel.objects.filter(default=True).exclude(channel_id=instance.
            channel_id).update(default=False)