def on_usb_device_detach(self, id_p, error):
    if not isinstance(id_p, basestring):
        raise TypeError('id_p can only be an instance of type basestring')
    if not isinstance(error, IVirtualBoxErrorInfo):
        raise TypeError(
            'error can only be an instance of type IVirtualBoxErrorInfo')
    self._call('onUSBDeviceDetach', in_p=[id_p, error])