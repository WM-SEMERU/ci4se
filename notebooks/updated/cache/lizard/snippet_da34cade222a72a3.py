def nvmlDeviceGetBridgeChipInfo(handle):
    r
    bridgeHierarchy = c_nvmlBridgeChipHierarchy_t()
    fn = _nvmlGetFunctionPointer('nvmlDeviceGetBridgeChipInfo')
    ret = fn(handle, byref(bridgeHierarchy))
    _nvmlCheckReturn(ret)
    return bytes_to_str(bridgeHierarchy)