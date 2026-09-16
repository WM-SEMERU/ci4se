def get_location(call=None, kwargs=None):
    if not kwargs:
        kwargs = {}
    vm_dict = get_configured_provider()
    vm_dict.update(kwargs)
    return config.get_cloud_config_value('location', vm_dict, __opts__,
        search_global=False)