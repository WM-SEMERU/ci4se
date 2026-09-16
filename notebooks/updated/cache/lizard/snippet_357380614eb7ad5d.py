def stat_container(self, container):
    LOG.debug('stat_container() with %s is success.', self.driver)
    return self.driver.stat_container(container)