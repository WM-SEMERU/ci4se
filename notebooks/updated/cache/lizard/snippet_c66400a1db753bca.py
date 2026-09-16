def _stop_consumers(self, number_of_consumers=0):
    while len(self._consumers) > number_of_consumers:
        consumer = self._consumers.pop()
        consumer.stop()