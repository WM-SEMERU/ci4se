def GetMemReservationMB(self):
    counter = c_uint()
    ret = vmGuestLib.VMGuestLib_GetMemReservationMB(self.handle.value,
        byref(counter))
    if ret != VMGUESTLIB_ERROR_SUCCESS:
        raise VMGuestLibException(ret)
    return counter.value