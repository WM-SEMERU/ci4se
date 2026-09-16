def _as_chunk(self):
    extra_bits = int_from_bytes(self.contents[0:1])
    bit_string = '{0:b}'.format(int_from_bytes(self.contents[1:]))
    mod_bit_len = len(bit_string) % 8
    if mod_bit_len != 0:
        bit_string = '0' * (8 - mod_bit_len) + bit_string
    if extra_bits > 0:
        return bit_string[0:0 - extra_bits]
    return bit_string