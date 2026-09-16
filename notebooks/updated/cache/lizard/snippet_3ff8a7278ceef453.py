def get_ports_by_name(device_name):
    filtered_devices = filter(lambda device: device_name in device[1],
        list_ports.comports())
    device_ports = [device[0] for device in filtered_devices]
    return device_ports