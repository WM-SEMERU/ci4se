def get_devices(self, force_reload=False, save_devices=True):
    if not os.path.exists(self._devices_filename) or force_reload is True:
        log.debug('getting devices from LaMetric cloud...')
        _, url = CLOUD_URLS['get_devices']
        res = self._cloud_session.session.get(url)
        if res is not None:
            res.raise_for_status()
        self._devices = res.json()
        if save_devices is True:
            self.save_devices()
        return self._devices
    else:
        log.debug("getting devices from '{}'...".format(self._devices_filename)
            )
        return self.load_devices()