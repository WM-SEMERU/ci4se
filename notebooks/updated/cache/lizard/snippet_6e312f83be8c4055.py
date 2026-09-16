def open_usb_handle(self, port_num):
    serial = self.get_usb_serial(port_num)
    return local_usb.LibUsbHandle.open(serial_number=serial)