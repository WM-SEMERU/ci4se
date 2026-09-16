def delete_renditions_if_master_has_changed(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if not obj.master == instance.master:
            obj.master.delete(save=False)
            instance.delete_all_renditions()