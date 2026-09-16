def profile_config_delete(name, config_key, remote_addr=None, cert=None,
    key=None, verify_cert=True):
    profile = profile_get(name, remote_addr, cert, key, verify_cert, _raw=True)
    return _delete_property_dict_item(profile, 'config', config_key)