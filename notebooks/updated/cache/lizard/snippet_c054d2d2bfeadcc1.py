def Write(self, packet):
    if len(packet) != self.GetOutReportDataLength():
        raise errors.HidError('Packet length must match report data length.')
    packet_data = [0] + packet
    out = bytes(bytearray(packet_data))
    num_written = wintypes.DWORD()
    ret = kernel32.WriteFile(self.dev, out, len(out), ctypes.byref(
        num_written), None)
    if num_written.value != len(out):
        raise errors.HidError('Failed to write complete packet.  ' + 
            'Expected %d, but got %d' % (len(out), num_written.value))
    if not ret:
        raise ctypes.WinError()