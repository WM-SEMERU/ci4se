def set_limit(self, param):
    limit = int(param)
    if -2000 <= limit <= 6000:
        self.device.temperature_limit = limit / 10.0
    return ''