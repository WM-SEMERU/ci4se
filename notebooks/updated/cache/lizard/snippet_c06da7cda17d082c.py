def target(self):
    while self.event.wait():
        self.event.clear()
        while True:
            with self.lock:
                if not self.count:
                    break
                self.count -= 1
            with self.condition:
                self.condition.notify_all()