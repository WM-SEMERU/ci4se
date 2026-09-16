def rackconnect(vm_):
    return config.get_cloud_config_value('rackconnect', vm_, __opts__,
        default=False, search_global=False)