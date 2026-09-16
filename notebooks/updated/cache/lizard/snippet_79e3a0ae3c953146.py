def reshape_by_device(x, num_devices):
    return layers.nested_map(x, lambda x: _reshape_by_device_single(x,
        num_devices))