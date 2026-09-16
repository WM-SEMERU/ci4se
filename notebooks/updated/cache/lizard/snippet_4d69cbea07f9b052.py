def unregisterWorker(self, name):
    if not name in self.worker_list:
        self.logger.error('Worker {0} is not registered!'.format(name))
        raise Exception('Worker {0} is not registered!'.format(name))
    del self.worker_list[name]
    self.logger.debug('Unregistered worker {0}'.format(name))