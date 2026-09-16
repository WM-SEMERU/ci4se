def _declareTimeoutExceeded(self, ev_data: RestartLogData):
    logger.info('Timeout exceeded for {}'.format(ev_data.when))
    last = self._actionLog.last_event
    if (last and last.ev_type == RestartLog.Events.failed and last.data ==
        ev_data):
        return None
    self._action_failed(ev_data, reason='exceeded restart timeout')
    self._unscheduleAction()
    self._actionFailedCallback()