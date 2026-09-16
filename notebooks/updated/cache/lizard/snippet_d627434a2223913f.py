def save_loop(self):
    last_hash = hash(repr(self.hosts))
    while self.running:
        eventlet.sleep(self.save_interval)
        next_hash = hash(repr(self.hosts))
        if next_hash != last_hash:
            self.save()
            last_hash = next_hash