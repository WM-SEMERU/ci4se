def live_log_child(self):
    if not (self.log_child and self.pid_is_alive(self.log_child)):
        self.start_log_child()