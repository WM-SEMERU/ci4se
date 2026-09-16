def listports():
    detected = False
    for port in serial.tools.list_ports.comports():
        detected = True
        if port.vid:
            micropythonPort = ''
            if is_micropython_usb_device(port):
                micropythonPort = ' *'
            print('USB Serial Device {:04x}:{:04x}{} found @{}{}\r'.format(
                port.vid, port.pid, extra_info(port), port.device,
                micropythonPort))
        else:
            print('Serial Device:', port.device)
    if not detected:
        print('No serial devices detected')