def set_pending_symbol(self, pending_symbol=None):
    if pending_symbol is None:
        pending_symbol = CodePointArray()
    self.value = bytearray()
    self.pending_symbol = pending_symbol
    self.line_comment = False
    return self