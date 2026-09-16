def convert(self):
    c = self.config
    c &= ~MCP342x._continuous_mode_mask & 127
    c |= MCP342x._not_ready_mask
    logger.debug('Convert ' + hex(self.address) + ' config: ' + bin(c))
    self.bus.write_byte(self.address, c)