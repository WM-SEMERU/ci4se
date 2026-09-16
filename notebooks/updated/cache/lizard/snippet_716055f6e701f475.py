def cmd_ublox_reset(self, args):
    print('Sending uBlox reset')
    msg = struct.pack('<HBB', 65535, 0, 0)
    self.master.mav.gps_inject_data_send(self.target_system, self.
        target_component, len(msg), bytearray(msg.ljust(110, '\x00')))