def wait_new_conf(self):
    logger.debug('Wait new configuration for %s, %s %s', self.name, self.
        alive, self.reachable)
    return self.con.get('_wait_new_conf')