def migrateUp(self):
    te = self.store.findFirst(TimedEvent, sort=TimedEvent.time.descending)
    if te is not None:
        self._transientSchedule(te.time, None)