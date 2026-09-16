def dump_logs(self):
    msg = 'log dump: \n'
    if self._transcribe:
        if self._transcribe_queue:
            while not self._transcribe_queue.empty():
                logs = self._transcribe_queue.get()
                if isinstance(logs, six.binary_type):
                    logs = logs.decode(encoding='UTF-8', errors='ignore')
                msg = '{0} {1}'.format(msg, logs)
    else:
        logs = self.client.logs(self.id, stdout=True, stderr=True, stream=
            False, timestamps=False, tail='all')
        if isinstance(logs, six.binary_type):
            logs = logs.decode(encoding='UTF-8', errors='ignore')
        msg = '{0}{1}'.format(msg, logs)
    logger.error(msg)