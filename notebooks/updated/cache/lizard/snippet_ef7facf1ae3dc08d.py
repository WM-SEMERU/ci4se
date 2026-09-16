def write_flash(self, addr, page_buffer, target_page, page_count):
    pk = None
    pk = self.link.receive_packet(0)
    while pk is not None:
        pk = self.link.receive_packet(0)
    retry_counter = 5
    while (not pk or pk.header != 255 or struct.unpack('<BB', pk.data[0:2]) !=
        (addr, 24)) and retry_counter >= 0:
        pk = CRTPPacket()
        pk.set_header(255, 255)
        pk.data = struct.pack('<BBHHH', addr, 24, page_buffer, target_page,
            page_count)
        self.link.send_packet(pk)
        pk = self.link.receive_packet(1)
        retry_counter -= 1
    if retry_counter < 0:
        self.error_code = -1
        return False
    self.error_code = pk.data[3]
    return pk.data[2] == 1