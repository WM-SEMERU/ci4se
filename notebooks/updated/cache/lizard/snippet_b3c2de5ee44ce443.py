def unpack(self, buff=None, offset=0):
    length = UBInt16()
    length.unpack(buff, offset)
    super().unpack(buff[:offset + length.value], offset)