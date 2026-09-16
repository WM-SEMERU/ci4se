def get_device(opts, salt_obj=None):
    log.debug('Setting up NAPALM connection')
    network_device = get_device_opts(opts, salt_obj=salt_obj)
    provider_lib = napalm_base
    if network_device.get('PROVIDER'):
        try:
            provider_lib = importlib.import_module(network_device.get(
                'PROVIDER'))
        except ImportError as ierr:
            log.error('Unable to import %s', network_device.get('PROVIDER'),
                exc_info=True)
            log.error('Falling back to napalm-base')
    _driver_ = provider_lib.get_network_driver(network_device.get(
        'DRIVER_NAME'))
    try:
        network_device['DRIVER'] = _driver_(network_device.get('HOSTNAME',
            ''), network_device.get('USERNAME', ''), network_device.get(
            'PASSWORD', ''), timeout=network_device['TIMEOUT'],
            optional_args=network_device['OPTIONAL_ARGS'])
        network_device.get('DRIVER').open()
        network_device['UP'] = True
    except napalm_base.exceptions.ConnectionException as error:
        base_err_msg = ('Cannot connect to {hostname}{port} as {username}.'
            .format(hostname=network_device.get('HOSTNAME',
            '[unspecified hostname]'), port=':{port}'.format(port=
            network_device.get('OPTIONAL_ARGS', {}).get('port')) if
            network_device.get('OPTIONAL_ARGS', {}).get('port') else '',
            username=network_device.get('USERNAME', '')))
        log.error(base_err_msg)
        log.error('Please check error: %s', error)
        raise napalm_base.exceptions.ConnectionException(base_err_msg)
    return network_device