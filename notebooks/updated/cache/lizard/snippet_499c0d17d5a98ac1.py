def set_script_timeout(self, time_to_wait):
    if self.w3c:
        self.execute(Command.SET_TIMEOUTS, {'script': int(float(
            time_to_wait) * 1000)})
    else:
        self.execute(Command.SET_SCRIPT_TIMEOUT, {'ms': float(time_to_wait) *
            1000})