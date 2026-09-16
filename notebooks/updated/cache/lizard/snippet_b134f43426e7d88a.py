def pulse_width(self):
    if self.pwm_device.pin.frequency is None:
        return None
    else:
        return self.pwm_device.pin.state * self.frame_width