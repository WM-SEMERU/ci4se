def create_server(self, basename, disk_image_id, instance_type,
    ssh_key_name, tags=None, availability_zone=None, timeout_s=
    DEFAULT_TIMEOUT_S, **provider_extras):
    log.info('Launching server %s... this could take a while...' % basename)
    if 'disable_api_termination' not in provider_extras:
        provider_extras['disable_api_termination'] = True
    if 'subnet_id' in provider_extras:
        secgroups = provider_extras.pop('security_groups', None)
        if secgroups:
            log.warn(
                '... When using subnet_id you must use security_group_ids.  Ignoring security_groups %s.'
                 % secgroups)
    res = self.ec2.run_instances(disk_image_id, instance_type=instance_type,
        key_name=ssh_key_name, placement=availability_zone, **provider_extras)
    instance = res.instances[0]
    time.sleep(2)

    def apply_tags():
        try:
            for key, val in tags.items():
                instance.add_tag(key, val)
            return True
        except EC2ResponseError:
            pass
    if not poll_with_timeout(timeout_s, apply_tags, 5):
        raise TimeoutError('Could not tag server %s' % instance.id)

    def find_running_instance():
        if instance.update() == 'running':
            return instance
    running = poll_with_timeout(timeout_s, find_running_instance, 5)
    if not running:
        raise TimeoutError('Could not launch server within allotted time.')
    return server_to_dict(running)