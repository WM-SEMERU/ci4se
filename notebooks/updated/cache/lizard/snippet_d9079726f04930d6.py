def scaled_pressure_send(self, time_boot_ms, press_abs, press_diff,
    temperature, force_mavlink1=False):
    return self.send(self.scaled_pressure_encode(time_boot_ms, press_abs,
        press_diff, temperature), force_mavlink1=force_mavlink1)