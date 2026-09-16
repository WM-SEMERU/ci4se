def single_device(cl_device_type='GPU', platform=None,
    fallback_to_any_device_type=False):
    if isinstance(cl_device_type, str):
        cl_device_type = device_type_from_string(cl_device_type)
    device = None
    if platform is None:
        platforms = cl.get_platforms()
    else:
        platforms = [platform]
    for platform in platforms:
        devices = platform.get_devices(device_type=cl_device_type)
        for dev in devices:
            if device_supports_double(dev):
                try:
                    env = CLEnvironment(platform, dev)
                    return [env]
                except cl.RuntimeError:
                    pass
    if not device:
        if fallback_to_any_device_type:
            return cl.get_platforms()[0].get_devices()
        else:
            raise ValueError('No devices of the specified type ({}) found.'
                .format(cl.device_type.to_string(cl_device_type)))
    raise ValueError('No suitable OpenCL device found.')