def wait_until_running(self, callback=None):
    status = self.machine.scheduler.wait_until_running(self.job, self.
        worker_config.time_out)
    if status.running:
        self.online = True
        if callback:
            callback(self)
    else:
        raise TimeoutError('Timeout while waiting for worker to run: ' +
            self.worker_config.name)