def get_consumers(self, _Consumer, channel):
    return [_Consumer(queues=[self.queue(channel)], callbacks=[self.
        main_callback], prefetch_count=self.prefetch_count)]