def grains():
    if not DETAILS.get('grains_cache', {}):
        DETAILS['grains_cache'] = GRAINS_CACHE
        try:
            compute_rack = get_config_resolver_class('computeRackUnit', False)
            DETAILS['grains_cache'] = compute_rack['outConfigs'][
                'computeRackUnit']
        except salt.exceptions.CommandExecutionError:
            pass
        except Exception as err:
            log.error(err)
    return DETAILS['grains_cache']