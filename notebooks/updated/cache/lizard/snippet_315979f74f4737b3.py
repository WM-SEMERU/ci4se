def stop(self):
    logger.info('is being stopped', extra={'formatter': 'container',
        'container': self.name})
    response = self.client.stop(self.id)
    while self.state()['running']:
        time.sleep(1)
    return response