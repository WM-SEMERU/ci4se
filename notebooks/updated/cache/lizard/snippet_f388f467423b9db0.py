def _setup_opera(self, capabilities):
    opera_driver = self.config.get('Driver', 'opera_driver_path')
    self.logger.debug('Opera driver path given in properties: %s', opera_driver
        )
    return webdriver.Opera(executable_path=opera_driver,
        desired_capabilities=capabilities)