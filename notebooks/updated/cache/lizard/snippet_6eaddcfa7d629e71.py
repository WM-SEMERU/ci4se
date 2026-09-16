def _update_battery_status(self, message=None, status=None):
    battery_status = status
    if isinstance(message, Message):
        battery_status = message.battery_low
    if battery_status is None:
        return
    last_status, last_update = self._battery_status
    if battery_status == last_status:
        self._battery_status = last_status, time.time()
    elif battery_status is True or time.time(
        ) > last_update + self._battery_timeout:
        self._battery_status = battery_status, time.time()
        self.on_low_battery(status=battery_status)
    return self._battery_status[0]