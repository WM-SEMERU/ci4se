def autoconnect_thread(monitor):
    monitor.start()
    monitor.filter_by('tty')
    epoll = select.epoll()
    epoll.register(monitor.fileno(), select.POLLIN)
    while True:
        try:
            events = epoll.poll()
        except InterruptedError:
            continue
        for fileno, _ in events:
            if fileno == monitor.fileno():
                usb_dev = monitor.poll()
                print('autoconnect: {} action: {}'.format(usb_dev.
                    device_node, usb_dev.action))
                dev = find_serial_device_by_port(usb_dev.device_node)
                if usb_dev.action == 'add':
                    for i in range(8):
                        if dev:
                            connected = connect_serial(dev.port, dev.baud,
                                dev.wait)
                        elif is_micropython_usb_device(usb_dev):
                            connected = connect_serial(usb_dev.device_node)
                        else:
                            connected = False
                        if connected:
                            break
                        time.sleep(0.25)
                elif usb_dev.action == 'remove':
                    print('')
                    print("USB Serial device '%s' disconnected" % usb_dev.
                        device_node)
                    if dev:
                        dev.close()
                        break