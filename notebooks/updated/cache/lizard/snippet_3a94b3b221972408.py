def set_setting(self, setting, value, area='1', validate_value=True):
    setting = setting.lower()
    if setting not in CONST.ALL_SETTINGS:
        raise AbodeException(ERROR.INVALID_SETTING, CONST.ALL_SETTINGS)
    if setting in CONST.PANEL_SETTINGS:
        url = CONST.SETTINGS_URL
        data = self._panel_settings(setting, value, validate_value)
    elif setting in CONST.AREA_SETTINGS:
        url = CONST.AREAS_URL
        data = self._area_settings(area, setting, value, validate_value)
    elif setting in CONST.SOUND_SETTINGS:
        url = CONST.SOUNDS_URL
        data = self._sound_settings(area, setting, value, validate_value)
    elif setting in CONST.SIREN_SETTINGS:
        url = CONST.SIREN_URL
        data = self._siren_settings(setting, value, validate_value)
    return self.send_request(method='put', url=url, data=data)