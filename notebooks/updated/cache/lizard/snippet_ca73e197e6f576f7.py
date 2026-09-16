def start(instance_id, call=None):
    if call != 'action':
        raise SaltCloudSystemExit(
            'The stop action must be called with -a or --action.')
    log.info('Starting instance %s', instance_id)
    params = {'action': 'StartInstances', 'zone': _get_specified_zone(
        provider=get_configured_provider()), 'instances.1': instance_id}
    result = query(params)
    return result