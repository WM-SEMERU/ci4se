def http_daemon_thread(self):
    logger.debug('HTTP thread running')
    try:
        self.http_daemon.run()
    except PortNotFree as exp:
        logger.exception('The HTTP daemon port is not free: %s', exp)
        raise
    except Exception as exp:
        self.exit_on_exception(exp)
    logger.debug('HTTP thread exiting')