def delay(self, seconds=0, minutes=0, msg=None):
    delay_time = seconds + minutes * 60
    self._hw_manager.hardware.delay(delay_time)