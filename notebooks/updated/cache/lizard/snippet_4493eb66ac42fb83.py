def getMaxPacketSize(self, endpoint):
    result = libusb1.libusb_get_max_packet_size(self.device_p, endpoint)
    mayRaiseUSBError(result)
    return result