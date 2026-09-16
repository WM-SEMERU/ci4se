def find_all(cls, vid=None, pid=None):
    if not have_pyftdi:
        raise ImportError(
            'The USBDevice class has been disabled due to missing requirement: pyftdi or pyusb.'
            )
    cls.__devices = []
    query = cls.PRODUCT_IDS
    if vid and pid:
        query = [(vid, pid)]
    try:
        cls.__devices = Ftdi.find_all(query, nocache=True)
    except (usb.core.USBError, FtdiError) as err:
        raise CommError('Error enumerating AD2USB devices: {0}'.format(str(
            err)), err)
    return cls.__devices