def write_block_data(self, address, register, value):
    return self.smbus.write_block_data(address, register, value)