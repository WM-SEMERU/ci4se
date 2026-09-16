def remove_usb_controller(self, name):
    if not isinstance(name, basestring):
        raise TypeError('name can only be an instance of type basestring')
    self._call('removeUSBController', in_p=[name])