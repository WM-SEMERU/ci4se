def stop_refresh(self):
    self.logger.debug('stopping timed refresh')
    self.rf_flags['done'] = True
    self.rf_timer.clear()