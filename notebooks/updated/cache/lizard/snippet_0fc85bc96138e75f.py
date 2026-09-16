def start(self):
    logging.info('TCP health monitor plugin: Starting to watch instances.')
    self.monitor_thread = threading.Thread(target=self.start_monitoring,
        name=self.thread_name)
    self.monitor_thread.daemon = True
    self.monitor_thread.start()