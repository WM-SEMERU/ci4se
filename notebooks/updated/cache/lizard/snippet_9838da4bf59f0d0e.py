def stop(self):
    if self.container_id is None:
        raise Exception('No Docker Selenium container was running')
    check_call(['docker', 'stop', self.container_id])
    self.container_id = None