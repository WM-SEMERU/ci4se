def shutdown(self, join=True, timeout=None):
    if self.is_alive():
        print('Shutdown initiated')
        self.exit.set()
        if join:
            self.join(timeout=timeout)
    exitcode = self._process.exitcode if self._process else None
    return exitcode