def nvmlDeviceGetTemperatureThreshold(handle, threshold):
    r
    c_temp = c_uint()
    fn = _nvmlGetFunctionPointer('nvmlDeviceGetTemperatureThreshold')
    ret = fn(handle, _nvmlTemperatureThresholds_t(threshold), byref(c_temp))
    _nvmlCheckReturn(ret)
    return bytes_to_str(c_temp.value)