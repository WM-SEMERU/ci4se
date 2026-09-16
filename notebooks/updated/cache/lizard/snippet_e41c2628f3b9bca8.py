def _time_up(self):
    self.running = False
    self.color = self.py3.COLOR_BAD
    self.time_left = 0
    self.done = True
    if self.sound:
        self.py3.play_sound(self.sound)
        self.alarm = True
    self.timer()