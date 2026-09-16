def register_exception(self, task, raised_exception, exception_details,
    event_details=None):
    if self.record_exception() is True:
        record = WSimpleTrackerStorage.ExceptionRecord(task,
            raised_exception, exception_details, event_details=event_details)
        self.__store_record(record)