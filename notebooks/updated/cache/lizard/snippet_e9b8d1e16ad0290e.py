def yieldable(self):
    if self.read_buffer is None:
        return False
    t = _remove_trailing_new_line(self.read_buffer)
    n = _find_furthest_new_line(t)
    if n >= 0:
        return True
    if self.read_position == 0 and self.read_buffer is not None:
        return True
    return False