def stop_request(self, stop_now=False):
    all_ok = True
    for daemon_link in self.all_daemons_links:
        logger.debug('Stopping: %s (%s)', daemon_link, stop_now)
        if daemon_link == self.arbiter_link:
            continue
        if not daemon_link.active:
            continue
        try:
            stop_ok = daemon_link.stop_request(stop_now=stop_now)
        except LinkError:
            stop_ok = True
            logger.warning('Daemon stop request failed, %s probably stopped!',
                daemon_link)
        all_ok = all_ok and stop_ok
        daemon_link.stopping = True
    self.stop_request_sent = all_ok
    return self.stop_request_sent