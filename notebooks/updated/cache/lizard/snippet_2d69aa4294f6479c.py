def close(self):
    if self._controller is not None:
        self._controller.quit()
        self._controller = None
    if self._process is not None:
        self._process.close()
        self._process = None