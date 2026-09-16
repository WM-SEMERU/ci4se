def reduce_by_device(parallelism, data, reduce_fn):
    unique_devices = []
    device_to_data = {}
    for dev, datum in zip(parallelism.devices, data):
        if dev not in device_to_data:
            unique_devices.append(dev)
            device_to_data[dev] = [datum]
        else:
            device_to_data[dev].append(datum)
    device_parallelism = Parallelism(unique_devices)
    grouped_data = [device_to_data[dev] for dev in unique_devices]
    return device_parallelism, device_parallelism(reduce_fn, grouped_data)