def flush(self, error=False, prompt=False):
    PythonShellWidget.flush(self, error=error, prompt=prompt)
    if self.interrupted:
        self.interrupted = False
        raise KeyboardInterrupt