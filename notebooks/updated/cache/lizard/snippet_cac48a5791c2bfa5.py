def OpenHandle(self):
    if hasattr(self, 'handle'):
        return self.handle
    else:
        handle = c_void_p()
        ret = vmGuestLib.VMGuestLib_OpenHandle(byref(handle))
        if ret != VMGUESTLIB_ERROR_SUCCESS:
            raise VMGuestLibException(ret)
        return handle