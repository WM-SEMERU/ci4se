def _set_scan_parameters(self, interval=2100, window=2100, active=False):
    active_num = 0
    if bool(active):
        active_num = 1
    interval_num = int(interval * 1000 / 625)
    window_num = int(window * 1000 / 625)
    payload = struct.pack('<HHB', interval_num, window_num, active_num)
    try:
        response = self._send_command(6, 7, payload)
        if response.payload[0] != 0:
            return False, {'reason': 'Could not set scanning parameters',
                'error': response.payload[0]}
    except InternalTimeoutError:
        return False, {'reason': 'Timeout waiting for response'}
    return True, None