def GenerateCalendarDatesFieldValuesTuples(self):
    for date, (exception_type, _) in self.date_exceptions.items():
        yield self.service_id, date, unicode(exception_type)