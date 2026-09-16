def kill(self, id, signal=signal.SIGTERM):
    args = {'id': id, 'signal': int(signal)}
    self._kill_chk.check(args)
    return self._client.json('job.kill', args)