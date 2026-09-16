def _apply_dvs_config(config_spec, config_dict):
    if config_dict.get('name'):
        config_spec.name = config_dict['name']
    if config_dict.get('contact_email') or config_dict.get('contact_name'):
        if not config_spec.contact:
            config_spec.contact = vim.DVSContactInfo()
        config_spec.contact.contact = config_dict.get('contact_email')
        config_spec.contact.name = config_dict.get('contact_name')
    if config_dict.get('description'):
        config_spec.description = config_dict.get('description')
    if config_dict.get('max_mtu'):
        config_spec.maxMtu = config_dict.get('max_mtu')
    if config_dict.get('lacp_api_version'):
        config_spec.lacpApiVersion = config_dict.get('lacp_api_version')
    if config_dict.get('network_resource_control_version'):
        config_spec.networkResourceControlVersion = config_dict.get(
            'network_resource_control_version')
    if config_dict.get('uplink_names'):
        if not config_spec.uplinkPortPolicy or not isinstance(config_spec.
            uplinkPortPolicy, vim.DVSNameArrayUplinkPortPolicy):
            config_spec.uplinkPortPolicy = vim.DVSNameArrayUplinkPortPolicy()
        config_spec.uplinkPortPolicy.uplinkPortName = config_dict[
            'uplink_names']