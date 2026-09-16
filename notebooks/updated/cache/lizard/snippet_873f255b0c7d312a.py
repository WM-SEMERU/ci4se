def write(self, fptr):
    self._validate(writing=True)
    bytes_per_row = sum(self.bits_per_component) / 8
    bytes_per_palette = bytes_per_row * self.palette.shape[0]
    box_length = 8 + 3 + self.palette.shape[1] + bytes_per_palette
    write_buffer = struct.pack('>I4s', int(box_length), b'pclr')
    fptr.write(write_buffer)
    write_buffer = struct.pack('>HB', self.palette.shape[0], self.palette.
        shape[1])
    fptr.write(write_buffer)
    bps_signed = [(x - 1) for x in self.bits_per_component]
    write_buffer = struct.pack('>' + 'B' * self.palette.shape[1], *bps_signed)
    fptr.write(write_buffer)
    fptr.write(memoryview(self.palette))