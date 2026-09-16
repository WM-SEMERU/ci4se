def container_device_add(name, device_name, device_type='disk', remote_addr
    =None, cert=None, key=None, verify_cert=True, **kwargs):
    container = container_get(name, remote_addr, cert, key, verify_cert,
        _raw=True)
    kwargs['type'] = device_type
    return _set_property_dict_item(container, 'devices', device_name, kwargs)