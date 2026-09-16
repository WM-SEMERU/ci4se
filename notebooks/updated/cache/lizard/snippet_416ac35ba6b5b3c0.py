def abort(self):
    self.print_active_threads()
    self.cancel()
    timeout = self.config['aborttimeout']
    try:
        self.urlqueue.join(timeout=timeout)
    except urlqueue.Timeout:
        log.warn(LOG_CHECK, 
            'Abort timed out after %d seconds, stopping application.' % timeout
            )
        raise KeyboardInterrupt()