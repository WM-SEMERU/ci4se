def find_raw_devices(vendor=None, product=None, serial_number=None,
    custom_match=None, **kwargs):

    def is_usbraw(dev):
        if custom_match and not custom_match(dev):
            return False
        return bool(find_interfaces(dev, bInterfaceClass=255,
            bInterfaceSubClass=255))
    return find_devices(vendor, product, serial_number, is_usbraw, **kwargs)