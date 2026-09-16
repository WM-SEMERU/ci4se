def find_usbserial(vendor, product):
    if platform.system() == 'Linux':
        vendor, product = [('%04x' % x).strip() for x in (vendor, product)]
        return linux_find_usbserial(vendor, product)
    elif platform.system() == 'Darwin':
        return osx_find_usbserial(vendor, product)
    else:
        raise NotImplementedError('Cannot find serial ports on %s' %
            platform.system())