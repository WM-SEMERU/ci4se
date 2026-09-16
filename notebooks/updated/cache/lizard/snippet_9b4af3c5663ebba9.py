def register_read_multiple(self, register_indices):
    num_regs = len(register_indices)
    buf = (ctypes.c_uint32 * num_regs)(*register_indices)
    data = (ctypes.c_uint32 * num_regs)(0)
    statuses = (ctypes.c_uint8 * num_regs)(0)
    res = self._dll.JLINKARM_ReadRegs(buf, data, statuses, num_regs)
    if res < 0:
        raise errors.JLinkException(res)
    return list(data)