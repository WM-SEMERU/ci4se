def handle_notification(self, data):
    _LOGGER.debug('Received notification from the device..')
    if data[0] == PROP_INFO_RETURN and data[1] == 1:
        _LOGGER.debug('Got status: %s' % codecs.encode(data, 'hex'))
        status = Status.parse(data)
        _LOGGER.debug('Parsed status: %s', status)
        self._raw_mode = status.mode
        self._valve_state = status.valve
        self._target_temperature = status.target_temp
        if status.mode.BOOST:
            self._mode = Mode.Boost
        elif status.mode.AWAY:
            self._mode = Mode.Away
            self._away_end = status.away
        elif status.mode.MANUAL:
            if status.target_temp == EQ3BT_OFF_TEMP:
                self._mode = Mode.Closed
            elif status.target_temp == EQ3BT_ON_TEMP:
                self._mode = Mode.Open
            else:
                self._mode = Mode.Manual
        else:
            self._mode = Mode.Auto
        _LOGGER.debug('Valve state: %s', self._valve_state)
        _LOGGER.debug('Mode:        %s', self.mode_readable)
        _LOGGER.debug('Target temp: %s', self._target_temperature)
        _LOGGER.debug('Away end:    %s', self._away_end)
    elif data[0] == PROP_SCHEDULE_RETURN:
        parsed = self.parse_schedule(data)
        self._schedule[parsed.day] = parsed
    else:
        _LOGGER.debug('Unknown notification %s (%s)', data[0], codecs.
            encode(data, 'hex'))