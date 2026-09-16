def terminate(self):
    logger.info('Sending SIGTERM to task {0}'.format(self.name))
    if hasattr(self, 'remote_client') and self.remote_client is not None:
        self.terminate_sent = True
        self.remote_client.close()
        return
    if not self.process:
        raise DagobahError('task does not have a running process')
    self.terminate_sent = True
    self.process.terminate()