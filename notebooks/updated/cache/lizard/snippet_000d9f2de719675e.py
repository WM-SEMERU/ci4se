def bytes(self):
    addrbyte = b'\x00\x00\x00'
    if self.addr is not None:
        addrbyte = self.addr
    return addrbyte