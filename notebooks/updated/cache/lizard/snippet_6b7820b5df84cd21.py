def width_at_offset(self, n):
    width = wcswidth(self.s[:n])
    assert width != -1
    return width