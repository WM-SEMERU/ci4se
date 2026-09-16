def setInterrupt(self, endpoint, buffer_or_len, callback=None, user_data=
    None, timeout=0):
    if self.__submitted:
        raise ValueError('Cannot alter a submitted transfer')
    if self.__doomed:
        raise DoomedTransferError('Cannot reuse a doomed transfer')
    string_buffer, self.__transfer_py_buffer = create_binary_buffer(
        buffer_or_len)
    self.__initialized = False
    self.__transfer_buffer = string_buffer
    self.__user_data = user_data
    libusb1.libusb_fill_interrupt_transfer(self.__transfer, self.__handle,
        endpoint, string_buffer, sizeof(string_buffer), self.
        __ctypesCallbackWrapper, None, timeout)
    self.__callback = callback
    self.__initialized = True