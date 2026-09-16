def tick(self):
    now = time.time()
    elapsed = now - self.latest_tick
    if elapsed > self.tick_interval:
        ticks = int(elapsed / self.tick_interval)
        self.tick_all(ticks)
        self.latest_tick = now