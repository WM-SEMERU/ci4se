def write_multiple_registers(self, regs_addr, regs_value):
    regs_nb = len(regs_value)
    if not 0 <= int(regs_addr) <= 65535:
        self.__debug_msg('write_multiple_registers(): regs_addr out of range')
        return None
    if not 1 <= int(regs_nb) <= 123:
        self.__debug_msg(
            'write_multiple_registers(): number of registers out of range')
        return None
    if int(regs_addr) + int(regs_nb) > 65536:
        self.__debug_msg('write_multiple_registers(): write after ad 65535')
        return None
    regs_val_str = b''
    for reg in regs_value:
        if not 0 <= int(reg) <= 65535:
            self.__debug_msg(
                'write_multiple_registers(): regs_value out of range')
            return None
        regs_val_str += struct.pack('>H', reg)
    bytes_nb = len(regs_val_str)
    body = struct.pack('>HHB', regs_addr, regs_nb, bytes_nb) + regs_val_str
    tx_buffer = self._mbus_frame(const.WRITE_MULTIPLE_REGISTERS, body)
    s_send = self._send_mbus(tx_buffer)
    if not s_send:
        return None
    f_body = self._recv_mbus()
    if not f_body:
        return None
    if len(f_body) != 4:
        self.__last_error = const.MB_RECV_ERR
        self.__debug_msg('write_multiple_registers(): rx frame size error')
        self.close()
        return None
    rx_reg_addr, rx_reg_nb = struct.unpack('>HH', f_body[:4])
    is_ok = rx_reg_addr == regs_addr
    return True if is_ok else None