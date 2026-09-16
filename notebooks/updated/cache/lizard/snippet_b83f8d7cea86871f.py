def get_current_state(self, clearConfig: bool=False):
    json_state = self.download_configuration()
    if 'errorCode' in json_state:
        LOGGER.error('Could not get the current configuration. Error: %s',
            json_state['errorCode'])
        return False
    if clearConfig:
        self.devices = []
        self.clients = []
        self.groups = []
        self.rules = []
        self.functionalHomes = []
    js_home = json_state['home']
    self.from_json(js_home)
    self._get_devices(json_state)
    self._get_clients(json_state)
    self._get_groups(json_state)
    self._get_functionalHomes(js_home)
    self._load_functionalChannels()
    return True