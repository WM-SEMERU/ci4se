def get_lb_conn(dd_driver=None):
    vm_ = get_configured_provider()
    region = config.get_cloud_config_value('region', vm_, __opts__)
    user_id = config.get_cloud_config_value('user_id', vm_, __opts__)
    key = config.get_cloud_config_value('key', vm_, __opts__)
    if not dd_driver:
        raise SaltCloudSystemExit(
            'Missing dimensiondata_driver for get_lb_conn method.')
    return get_driver_lb(Provider_lb.DIMENSIONDATA)(user_id, key, region=region
        )