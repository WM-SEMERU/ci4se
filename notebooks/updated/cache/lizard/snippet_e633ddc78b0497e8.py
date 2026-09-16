def GetHostCpuUsedMs(self):
    counter = c_uint64()
    ret = vmGuestLib.VMGuestLib_GetHostCpuUsedMs(self.handle.value, byref(
        counter))
    if ret != VMGUESTLIB_ERROR_SUCCESS:
        raise VMGuestLibException(ret)
    return counter.value