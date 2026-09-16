def set_flagged(self, *, start_date=None, due_date=None):
    self.__status = Flag.Flagged
    start_date = start_date or dt.datetime.now()
    due_date = due_date or dt.datetime.now()
    if start_date.tzinfo is None:
        start_date = self.protocol.timezone.localize(start_date)
    if due_date.tzinfo is None:
        due_date = self.protocol.timezone.localize(due_date)
    self.__start = start_date
    self.__due_date = due_date
    self._track_changes()