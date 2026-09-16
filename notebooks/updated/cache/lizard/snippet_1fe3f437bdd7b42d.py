def getNextTimeout(self):
    timeval = libusb1.timeval()
    result = libusb1.libusb_get_next_timeout(self.__context_p, byref(timeval))
    if result == 0:
        return None
    elif result == 1:
        return timeval.tv_sec + timeval.tv_usec * 1e-06
    raiseUSBError(result)