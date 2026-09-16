def stringify_device_meta(device_object):
    try:
        if isinstance(device_object['info']['description']['meta'], dict):
            device_object['info']['description']['meta'] = json.dumps(
                device_object['info']['description']['meta'])
    except ValueError as err:
        print('stringify: {0}'.format(err))
    return device_object