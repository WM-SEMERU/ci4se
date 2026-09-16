def _main_loop(self):
    while self.active:
        self.expire()
        if self.roll and self.is_expired():
            self.start_time = self.start_time + self.window
            self._set_key()
        self.purge_old()
        time.sleep(self.cycle_time)
    self._clean_up()