def daemonize(self):
    self._double_fork()
    self.pid = os.getpid()
    LOG.info('Succesfully daemonized process {0}.'.format(self.pid))