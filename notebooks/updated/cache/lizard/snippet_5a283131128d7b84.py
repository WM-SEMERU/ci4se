def start(self):
    t = threading.Thread(target=self._consume)
    t.start()