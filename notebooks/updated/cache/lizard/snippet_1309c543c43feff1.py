def get_times(self):
    send_time = ctypes.c_int32()
    recv_time = ctypes.c_int32()
    result = self.library.Par_GetTimes(self.pointer, ctypes.byref(send_time
        ), ctypes.byref(recv_time))
    check_error(result, 'partner')
    return send_time, recv_time