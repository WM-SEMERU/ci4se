def _load_controller_settings(self):
    try:
        if not os.path.exists(self._config_file):
            yield from self._import_gns3_gui_conf()
            self.save()
        with open(self._config_file) as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        log.critical('Cannot load %s: %s', self._config_file, str(e))
        self._settings = {}
        return []
    if 'settings' in data and data['settings'] is not None:
        self._settings = data['settings']
    else:
        self._settings = {}
    if 'gns3vm' in data:
        self.gns3vm.settings = data['gns3vm']
    self.load_appliances()
    return data.get('computes', [])