def _send_timer_stopped(self, lCall):
    if self._sendLooper is not lCall:
        log.warning('commitTimerStopped with wrong timer:%s not:%s', lCall,
            self._sendLooper)
    else:
        self._sendLooper = None
        self._sendLooperD = None