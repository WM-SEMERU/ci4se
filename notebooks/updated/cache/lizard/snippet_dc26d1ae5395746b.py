def set_driver_simulated(self):
    self._device_dict['servermain.MULTIPLE_TYPES_DEVICE_DRIVER'] = 'Simulator'
    if self._is_sixteen_bit:
        self._device_dict['servermain.DEVICE_MODEL'] = 0
    else:
        self._device_dict['servermain.DEVICE_MODEL'] = 1
    self._device_dict['servermain.DEVICE_ID_OCTAL'] = 1