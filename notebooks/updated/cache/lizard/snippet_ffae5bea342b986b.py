def set_default_mode(self, default_mode):
    if default_mode.lower() not in (CONST.MODE_AWAY, CONST.MODE_HOME):
        raise AbodeException(ERROR.INVALID_DEFAULT_ALARM_MODE)
    self._default_alarm_mode = default_mode.lower()