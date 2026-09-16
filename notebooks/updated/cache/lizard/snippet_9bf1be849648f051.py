def stop(self, wait=False):
    if self.instance_id is not None:
        log.info('Shutting down node `%s` (VM instance `%s`) ...', self.
            name, self.instance_id)
        self._cloud_provider.stop_instance(self.instance_id)
        if wait:
            while self.is_alive():
                time.sleep(1)
        self.instance_id = None