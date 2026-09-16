def _send_periodic_internal(self, msg, period, duration=None):
    if self._scheduler is None:
        self._scheduler = HANDLE()
        _canlib.canSchedulerOpen(self._device_handle, self.channel, self.
            _scheduler)
        caps = structures.CANCAPABILITIES()
        _canlib.canSchedulerGetCaps(self._scheduler, caps)
        self._scheduler_resolution = float(caps.dwClockFreq
            ) / caps.dwCmsDivisor
        _canlib.canSchedulerActivate(self._scheduler, constants.TRUE)
    return CyclicSendTask(self._scheduler, msg, period, duration, self.
        _scheduler_resolution)