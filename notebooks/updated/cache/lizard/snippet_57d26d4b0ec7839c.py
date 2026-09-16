def _start_scan(self, active):
    success, retval = self._set_scan_parameters(active=active)
    if not success:
        return success, retval
    try:
        response = self._send_command(6, 2, [2])
        if response.payload[0] != 0:
            self._logger.error('Error starting scan for devices, error=%d',
                response.payload[0])
            return False, {'reason': 
                'Could not initiate scan for ble devices, error_code=%d, response=%s'
                 % (response.payload[0], response)}
    except InternalTimeoutError:
        return False, {'reason': 'Timeout waiting for response'}
    return True, None