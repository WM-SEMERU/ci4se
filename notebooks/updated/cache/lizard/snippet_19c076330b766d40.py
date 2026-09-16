def notify(self, message):
    if self.complete:
        return HerokuLocalWrapper.MONITOR_STOP
    return super(DebugDeployment, self).notify(message)