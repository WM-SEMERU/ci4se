def task_postponed(self):
    tracker = self.task().tracker_storage()
    if tracker is not None and self.track_wait() is True:
        details = self.task().event_details(WTrackerEvents.wait)
        tracker.register_wait(self.task(), event_details=details)
    WScheduleRecord.task_postponed(self)