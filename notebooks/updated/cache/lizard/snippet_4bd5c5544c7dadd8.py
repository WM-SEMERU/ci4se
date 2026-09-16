def pwm_start(self, channel, duty_cycle=None, frequency=None):
    if frequency:
        self.set_pwm_freq(frequency)
    self.set_pwm(channel, 0, int(4096 * (duty_cycle / 100)))