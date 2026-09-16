def setup_consumers(self):
    if not self.consumer_cfg:
        LOGGER.warning('No consumers are configured')
    for name in self.consumer_cfg.keys():
        self.consumers[name] = self.new_consumer(self.consumer_cfg[name], name)
        self.start_processes(name, self.consumers[name].qty)