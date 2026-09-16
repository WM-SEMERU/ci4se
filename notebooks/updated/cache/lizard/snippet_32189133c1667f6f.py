def wait_for_vacancy(self, processor_type):
    with self._condition:
        self._condition.wait_for(lambda : self._processor_available(
            processor_type) or self._cancelled_event.is_set())
        if self._cancelled_event.is_set():
            raise WaitCancelledException()
        processor = self[processor_type].next_processor()
        return processor