def send_sysex(self, sysex_cmd, data):
    msg = bytearray([START_SYSEX, sysex_cmd])
    msg.extend(data)
    msg.append(END_SYSEX)
    self.sp.write(msg)