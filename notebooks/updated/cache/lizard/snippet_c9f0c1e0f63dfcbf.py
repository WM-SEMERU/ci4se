def GetEntries(self, parser_mediator, cookie_data=None, url=None, **kwargs):
    fields = cookie_data.split('.')
    number_of_fields = len(fields)
    if number_of_fields not in (1, 4):
        parser_mediator.ProduceExtractionWarning(
            'unsupported number of fields: {0:d} in cookie: {1:s}'.format(
            number_of_fields, self.COOKIE_NAME))
        return
    if number_of_fields == 1:
        domain_hash = None
        try:
            last_visit_posix_time = int(fields[0], 10) / 10000000
        except ValueError:
            last_visit_posix_time = None
        number_of_pages_viewed = None
    elif number_of_fields == 4:
        domain_hash = fields[0]
        try:
            number_of_pages_viewed = int(fields[1], 10)
        except ValueError:
            number_of_pages_viewed = None
        try:
            if fields[2] in ('8', '9'):
                last_visit_posix_time = int(fields[3], 10) / 1000
            else:
                last_visit_posix_time = int(fields[3], 10)
        except ValueError:
            last_visit_posix_time = None
    if last_visit_posix_time is not None:
        date_time = dfdatetime_posix_time.PosixTime(timestamp=
            last_visit_posix_time)
        timestamp_description = definitions.TIME_DESCRIPTION_LAST_VISITED
    else:
        date_time = dfdatetime_semantic_time.SemanticTime('Not set')
        timestamp_description = definitions.TIME_DESCRIPTION_NOT_A_TIME
    event_data = GoogleAnalyticsEventData('utmb')
    event_data.cookie_name = self.COOKIE_NAME
    event_data.domain_hash = domain_hash
    event_data.pages_viewed = number_of_pages_viewed
    event_data.url = url
    event = time_events.DateTimeValuesEvent(date_time, timestamp_description)
    parser_mediator.ProduceEventWithEventData(event, event_data)