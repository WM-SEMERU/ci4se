def connect_serial(port, baud=115200, wait=0):
    if not QUIET:
        print('Connecting to %s (buffer-size %d)...' % (port, BUFFER_SIZE))
    try:
        dev = DeviceSerial(port, baud, wait)
    except DeviceError as err:
        sys.stderr.write(str(err))
        sys.stderr.write('\n')
        return False
    add_device(dev)
    return True