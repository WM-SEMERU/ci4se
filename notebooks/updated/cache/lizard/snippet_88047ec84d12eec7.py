def hostname_is_compatible(conn, logger, provided_hostname):
    logger.debug('determining if provided host has same hostname in remote')
    remote_hostname = conn.remote_module.shortname()
    if remote_hostname == provided_hostname:
        return
    logger.warning('*' * 80)
    logger.warning('provided hostname must match remote hostname')
    logger.warning('provided hostname: %s' % provided_hostname)
    logger.warning('remote hostname: %s' % remote_hostname)
    logger.warning(
        'monitors may not reach quorum and create-keys will not complete')
    logger.warning('*' * 80)