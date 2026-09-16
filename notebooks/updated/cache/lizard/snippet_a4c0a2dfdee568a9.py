def scheduler(self, sleep_time=0.2):
    while self.listening:
        if self.scheduled_calls:
            timestamp = time.time()
            self.scheduled_calls[:] = [item for item in self.
                scheduled_calls if not self.time_reached(timestamp, item)]
        time.sleep(sleep_time)
    logger.info('Shutting down the call scheduler...')