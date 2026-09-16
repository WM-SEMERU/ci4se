def receive(self):
    while self.buffer.empty() and self.__up:
        sleep_ms = random.randint(0, 1000)
        time.sleep(sleep_ms / 1000.0)
    if not self.buffer.empty():
        return self.buffer.get(block=False)
    return '', ''