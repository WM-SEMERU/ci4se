def mark(self, partition, offset):
    max_offset = max(offset + 1, self.high_water_mark.get(partition, 0))
    self.logger.debug('Setting high-water mark to: %s', {partition: max_offset}
        )
    self.high_water_mark[partition] = max_offset