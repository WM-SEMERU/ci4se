def list(self):
    settings = []
    for setting in _SETTINGS:
        value = self.get(setting)
        is_set = self.is_set(setting)
        default_value = self.get_default_value(setting)
        is_supported = True
        settings.append((setting, value, default_value, is_set, is_supported))
    for setting in sorted(self.settings_state.list_keys()):
        if not self.is_supported(setting):
            value = self.get(setting)
            default_value = None
            is_set = True
            is_supported = False
            settings.append((setting, value, default_value, is_set,
                is_supported))
    return settings