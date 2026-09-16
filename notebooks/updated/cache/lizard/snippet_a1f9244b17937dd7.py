def find_all(pattern=None):
    devices = []
    try:
        if pattern:
            devices = serial.tools.list_ports.grep(pattern)
        else:
            devices = serial.tools.list_ports.comports()
    except serial.SerialException as err:
        raise CommError('Error enumerating serial devices: {0}'.format(str(
            err)), err)
    return devices