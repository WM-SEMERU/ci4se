def find_key(debug=False, skip=0):
    try:
        hid_device = YubiKeyHIDDevice(debug, skip)
        yk_version = hid_device.status().ykver()
        if (2, 1, 4) <= yk_version <= (2, 1, 9):
            return YubiKeyNEO_USBHID(debug, skip, hid_device)
        if yk_version < (3, 0, 0):
            return YubiKeyUSBHID(debug, skip, hid_device)
        if yk_version < (4, 0, 0):
            return YubiKeyNEO_USBHID(debug, skip, hid_device)
        return YubiKey4_USBHID(debug, skip, hid_device)
    except YubiKeyUSBHIDError as inst:
        if 'No USB YubiKey found' in str(inst):
            raise YubiKeyError('No YubiKey found')
        else:
            raise