def set_mode(self, mode):
    if not mode:
        raise AbodeException(ERROR.MISSING_ALARM_MODE)
    elif mode.lower() not in CONST.ALL_MODES:
        raise AbodeException(ERROR.INVALID_ALARM_MODE, CONST.ALL_MODES)
    mode = mode.lower()
    response = self._abode.send_request('put', CONST.get_panel_mode_url(
        self._area, mode))
    _LOGGER.debug('Set Alarm Home Response: %s', response.text)
    response_object = json.loads(response.text)
    if response_object['area'] != self._area:
        raise AbodeException(ERROR.SET_MODE_AREA)
    if response_object['mode'] != mode:
        raise AbodeException(ERROR.SET_MODE_MODE)
    self._json_state['mode'][self.device_id] = response_object['mode']
    _LOGGER.info('Set alarm %s mode to: %s', self._device_id,
        response_object['mode'])
    return True