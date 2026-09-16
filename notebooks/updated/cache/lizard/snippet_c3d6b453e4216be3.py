def cloudnetwork(vm_):
    return config.get_cloud_config_value('cloudnetwork', vm_, __opts__,
        default=False, search_global=False)