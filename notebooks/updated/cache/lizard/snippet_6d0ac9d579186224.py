def start_scan(self, active):
    self._command_task.sync_command(['_start_scan', active])
    self.scanning = True