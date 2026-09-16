def register_subarray_devices():
    tango_db = Database()
    LOG.info('Registering Subarray devices:')
    device_info = DbDevInfo()
    device_info._class = 'SubarrayDevice'
    device_info.server = 'subarray_ds/1'
    for index in range(16):
        device_info.name = 'sip_sdp/elt/subarray_{:02d}'.format(index)
        LOG.info('\t%s', device_info.name)
        tango_db.add_device(device_info)
    tango_db.put_class_property(device_info._class, dict(version='1.0.0'))