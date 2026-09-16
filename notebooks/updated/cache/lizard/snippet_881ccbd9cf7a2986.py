def _check_timers(self):
    if self._timer_queue:
        timer = self._timer_queue[0]
        if timer['timeout_abs'] < _current_time_millis():
            self._timer_queue.pop(0)
            self._logger.debug(
                'Timer {} expired for stm {}, adding it to event queue.'.
                format(timer['id'], timer['stm'].id))
            self._add_event(timer['id'], [], {}, timer['stm'], front=True)
        else:
            self._next_timeout = (timer['timeout_abs'] - _current_time_millis()
                ) / 1000
            if self._next_timeout < 0:
                self._next_timeout = 0
    else:
        self._next_timeout = None