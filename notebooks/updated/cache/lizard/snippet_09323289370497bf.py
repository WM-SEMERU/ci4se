def _head_length(self, port):
    if not port:
        return 0.0
    parent_state_v = self.get_parent_state_v()
    if parent_state_v is port.parent:
        return port.port_size[1]
    return max(port.port_size[1] * 1.5, self._calc_line_width() / 1.3)