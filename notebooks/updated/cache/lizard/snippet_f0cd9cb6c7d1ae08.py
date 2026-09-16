def get_next_batch(self):
    messages = self.get_from_kafka()
    if messages:
        for message in messages:
            item = BaseRecord(message)
            self.increase_read()
            yield item
    self.logger.debug('Done reading batch')
    self.last_position = self.consumer.offsets