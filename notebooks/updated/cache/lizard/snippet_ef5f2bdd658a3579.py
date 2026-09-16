def decode(self, fd, mtu, max_len=2560):
    output_buffer = ffi.new('char[]', max_len)
    sz = self.codec.rtp_sbc_decode_from_fd(self.config, output_buffer,
        max_len, mtu, fd)
    return ffi.buffer(output_buffer[0:sz])