def data_to_binary(self):
    if self.channel == 1:
        tmp = 3
    else:
        tmp = 12
    return bytes([COMMAND_CODE, tmp]) + struct.pack('>L', self.delay_time)[-3:]