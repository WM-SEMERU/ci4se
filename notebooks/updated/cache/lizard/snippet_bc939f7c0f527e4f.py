def write_reg(self, addr, value, mask=4294967295, delay_us=0):
    return self.check_command('write target memory', self.ESP_WRITE_REG,
        struct.pack('<IIII', addr, value, mask, delay_us))