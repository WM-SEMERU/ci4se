def _load_properties(property_name, config_option, set_default=False,
    default=None):
    if not property_name:
        log.debug(
            'No property specified in function, trying to load from salt configuration'
            )
        try:
            options = __salt__['config.option']('cassandra')
        except BaseException as e:
            log.error('Failed to get cassandra config options. Reason: %s', e)
            raise
        loaded_property = options.get(config_option)
        if not loaded_property:
            if set_default:
                log.debug('Setting default Cassandra %s to %s',
                    config_option, default)
                loaded_property = default
            else:
                log.error(
                    'No cassandra %s specified in the configuration or passed to the module.'
                    , config_option)
                raise CommandExecutionError(
                    'ERROR: Cassandra {0} cannot be empty.'.format(
                    config_option))
        return loaded_property
    return property_name