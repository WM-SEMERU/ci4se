def IsActiveOn(self, date, date_object=None):
    if date in self.date_exceptions:
        exception_type, _ = self.date_exceptions[date]
        if exception_type == self._EXCEPTION_TYPE_ADD:
            return True
        else:
            return False
    if (self.start_date and self.end_date and self.start_date <= date and 
        date <= self.end_date):
        if date_object is None:
            date_object = util.DateStringToDateObject(date)
        return self.day_of_week[date_object.weekday()]
    return False