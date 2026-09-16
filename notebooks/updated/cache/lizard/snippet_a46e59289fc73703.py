def load_page_buffer(self, buffer_number, address, bytes):
    assert buffer_number < len(self.page_buffers), 'Invalid buffer number'
    bytes = self.override_security_bits(address, bytes)
    self.target.write_memory_block8(self.page_buffers[buffer_number], bytes)