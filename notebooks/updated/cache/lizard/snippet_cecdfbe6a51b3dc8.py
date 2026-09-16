def power_on(self):
    try:
        self.send_command('POWER_ON')
        self._power = POWER_ON
        self._state = STATE_ON
        return True
    except requests.exceptions.RequestException:
        _LOGGER.error('Connection error: power on command not sent.')
        return False