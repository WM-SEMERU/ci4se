def _traceroute_callback(self, line, kill_switch):
    line = line.lower()
    if 'traceroute to' in line:
        self.started = True
    if 'enough privileges' in line:
        self.error = True
        self.kill_switch()
        self.stopped = True
    if 'service not known' in line:
        self.error = True
        self.kill_switch()
        self.stopped = True