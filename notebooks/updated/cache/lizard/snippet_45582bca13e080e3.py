def remove(self, name):
    init = self._get_implementation(name)
    self._assert_service_installed(init, name)
    logger.info('Removing %s service %s...', self.init_system, name)
    init.stop()
    init.uninstall()
    logger.info('Service removed')