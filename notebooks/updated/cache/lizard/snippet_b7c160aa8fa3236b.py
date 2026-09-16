def get_setting(self, key, default=NOT_SET):
    if self._arca is None:
        raise LazySettingProperty.SettingsNotReady
    return self._arca.settings.get(*self.get_settings_keys(key), default=
        default)