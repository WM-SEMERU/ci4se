def action_log_delete(sender, instance, **kwargs):
    if instance.pk is not None:
        changes = model_instance_diff(instance, None)
        log_entry = LogAction.objects.create_log_action(instance=instance,
            action=LogAction.DELETE, changes=json.dumps(changes))