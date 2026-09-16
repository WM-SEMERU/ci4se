def nvmlDeviceGetPowerUsage(handle):
    r
    c_watts = c_uint()
    fn = _nvmlGetFunctionPointer('nvmlDeviceGetPowerUsage')
    ret = fn(handle, byref(c_watts))
    _nvmlCheckReturn(ret)
    return bytes_to_str(c_watts.value)