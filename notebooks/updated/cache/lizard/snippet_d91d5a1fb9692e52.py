def create_image(ami_name, instance_id=None, instance_name=None, tags=None,
    region=None, key=None, keyid=None, profile=None, description=None,
    no_reboot=False, dry_run=False, filters=None):
    instances = find_instances(instance_id=instance_id, name=instance_name,
        tags=tags, region=region, key=key, keyid=keyid, profile=profile,
        return_objs=True, filters=filters)
    if not instances:
        log.error('Source instance not found')
        return False
    if len(instances) > 1:
        log.error(
            'Multiple instances found, must match exactly only one instance to create an image from'
            )
        return False
    instance = instances[0]
    try:
        return instance.create_image(ami_name, description=description,
            no_reboot=no_reboot, dry_run=dry_run)
    except boto.exception.BotoServerError as exc:
        log.error(exc)
        return False