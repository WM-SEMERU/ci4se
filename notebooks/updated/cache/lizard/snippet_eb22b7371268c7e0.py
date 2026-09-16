def current_settings(self):
    settings = {}
    if not self.status_data:
        return settings
    for key, val in self.status_data.get('curvals', {}).items():
        try:
            val = float(val)
        except ValueError:
            val = val
        if val in ('on', 'off'):
            val = val == 'on'
        settings[key] = val
    return settings