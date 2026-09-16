def print_status(self):
    tweets = self.received
    now = time.time()
    diff = now - self.since
    self.since = now
    self.received = 0
    if diff > 0:
        logger.info('Receiving tweets at %s tps', tweets / diff)