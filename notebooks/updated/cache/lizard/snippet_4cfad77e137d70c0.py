def set_cooling_motor(self, cooling_motor):
    if type(cooling_motor) != bool:
        raise InvalidInput('Cooling motor value must be bool')
    self._config['cooling_motor'] = bool2int(cooling_motor)
    self._q.put(self._config)