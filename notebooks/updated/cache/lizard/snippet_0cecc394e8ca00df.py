def _set_mode(self, discover_mode, connect_mode):
    payload = struct.pack('<BB', discover_mode, connect_mode)
    response = self._send_command(6, 1, payload)
    result, = unpack('<H', response.payload)
    if result != 0:
        return False, {'reason': 'Error code from BLED112 setting mode',
            'code': result}
    return True, None