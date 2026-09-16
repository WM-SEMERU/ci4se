def clean_up(self):
    if not self.started:
        return
    self.started = False
    self.clear_all_events()
    self._sl4a.disconnect()
    self.poller.set_result('Done')
    self.executor.shutdown(wait=False)