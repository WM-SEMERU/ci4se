def processEnded(self, reason):
    log_debug('{name} process exited', name=self.name)
    if self.deferred:
        if reason.type == ProcessDone:
            self.deferred.callback(reason.value.exitCode)
        elif reason.type == ProcessTerminated:
            self.deferred.errback(reason)
    return self.deferred