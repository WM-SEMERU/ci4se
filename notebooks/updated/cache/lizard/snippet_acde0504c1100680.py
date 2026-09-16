def install_json(self):
    if self._install_json is None:
        try:
            install_json_filename = os.path.join(os.getcwd(), 'install.json')
            with open(install_json_filename, 'r') as fh:
                self._install_json = json.load(fh)
        except IOError:
            self.log.warning('Could not retrieve App Data.')
            self._install_json = {}
    return self._install_json