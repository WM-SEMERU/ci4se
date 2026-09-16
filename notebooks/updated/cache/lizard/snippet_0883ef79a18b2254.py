def _device_to_sysfs_path(device):
    return '%s-%s' % (device.getBusNumber(), '.'.join([str(item) for item in
        device.GetPortNumberList()]))