def iter_open(cls, name=None, interface_class=None, interface_subclass=None,
    interface_protocol=None, serial_number=None, port_path=None,
    default_timeout_ms=None):
    ctx = usb1.USBContext()
    try:
        devices = ctx.getDeviceList(skip_on_error=True)
    except libusb1.USBError as exception:
        raise usb_exceptions.LibusbWrappingError(exception,
            'Open(name=%s, class=%s, subclass=%s, protocol=%s, serial=%s, port=%s) failed'
            , name, interface_class, interface_subclass, interface_protocol,
            serial_number, port_path)
    for device in devices:
        try:
            if serial_number is not None and device.getSerialNumber(
                ) != serial_number:
                continue
            if port_path is not None and cls._device_to_sysfs_path(device
                ) != port_path:
                continue
            for setting in device.iterSettings():
                if interface_class is not None and setting.getClass(
                    ) != interface_class:
                    continue
                if interface_subclass is not None and setting.getSubClass(
                    ) != interface_subclass:
                    continue
                if interface_protocol is not None and setting.getProtocol(
                    ) != interface_protocol:
                    continue
                yield cls(device, setting, name=name, default_timeout_ms=
                    default_timeout_ms)
        except libusb1.USBError as exception:
            if exception.value != libusb1.libusb_error.forward_dict[
                'LIBUSB_ERROR_ACCESS']:
                raise