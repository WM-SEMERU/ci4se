def switch_to_app(self, package):
    log.debug("switching to app '{}'...".format(package))
    cmd, url = DEVICE_URLS['switch_to_app']
    widget_id = self._get_widget_id(package)
    url = url.format('{}', package, widget_id)
    self.result = self._exec(cmd, url)