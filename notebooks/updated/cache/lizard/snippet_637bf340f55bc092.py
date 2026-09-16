def matrix(self):
    matrix = (c_float * 6)()
    rc = self._libinput.libinput_device_config_calibration_get_matrix(self.
        _handle, matrix)
    return rc, tuple(matrix)