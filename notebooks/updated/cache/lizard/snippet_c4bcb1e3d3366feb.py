def peek(self, session, address, width):
    if width == 8:
        return self.peek_8(session, address)
    elif width == 16:
        return self.peek_16(session, address)
    elif width == 32:
        return self.peek_32(session, address)
    elif width == 64:
        return self.peek_64(session, address)
    raise ValueError(
        '%s is not a valid size. Valid values are 8, 16, 32 or 64' % width)