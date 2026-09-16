def _on_process_started(self):
    comm('backend process started')
    if self is None:
        return
    self.starting = False
    self.running = True