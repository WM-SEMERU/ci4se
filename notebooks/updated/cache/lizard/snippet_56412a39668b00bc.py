def start(self, timeout=None):
    if not timeout:
        timeout = self.timeout
    self.thread.start()
    start_time = time.time()
    while start_time + timeout > time.time():
        self.thread.join(1)
        if self.error or self.started:
            break
    if self.started:
        logging.info('OpenVPN connected')
        OpenVPN.connected_instances.append(self)
    else:
        logging.warn('OpenVPN not started')
        for line in self.notifications.split('\n'):
            logging.warn('OpenVPN output:\t\t%s' % line)