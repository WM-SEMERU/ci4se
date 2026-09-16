def idle_task(self):
    for r in self.repeats:
        if r.event.trigger():
            self.mpstate.functions.process_stdin(r.cmd, immediate=True)