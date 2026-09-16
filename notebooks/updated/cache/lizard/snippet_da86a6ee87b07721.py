def start(self):
    if self.pid is not None:
        LOG.error('The process is already running with pid {0}.'.format(
            self.pid))
        sys.exit(exit.ALREADY_RUNNING)
    self.daemonize()
    LOG.info('Beginning run loop for process.')
    try:
        self.run()
    except Exception:
        LOG.exception('Uncaught exception in the daemon run() method.')
        self.stop()
        sys.exit(exit.RUN_FAILURE)