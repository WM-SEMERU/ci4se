def _load_custom(self, settings_name='localsettings.py'):
    if settings_name[-3:] == '.py':
        settings_name = settings_name[:-3]
    new_settings = {}
    try:
        settings = importlib.import_module(settings_name)
        new_settings = self._convert_to_dict(settings)
    except ImportError:
        log.info('No override settings found')
    for key in new_settings:
        if key in self.my_settings:
            item = new_settings[key]
            if isinstance(item, dict) and isinstance(self.my_settings[key],
                dict):
                for key2 in item:
                    self.my_settings[key][key2] = item[key2]
            else:
                self.my_settings[key] = item
        else:
            self.my_settings[key] = new_settings[key]