def read_events(self, calendar_ids=(), from_date=None, to_date=None,
    last_modified=None, tzid=settings.DEFAULT_TIMEZONE_ID, only_managed=
    False, include_managed=True, include_deleted=False, include_moved=False,
    include_geo=False, localized_times=False, automatic_pagination=True):
    results = self.request_handler.get(endpoint='events', params={'tzid':
        tzid, 'calendar_ids[]': calendar_ids, 'from': format_event_time(
        from_date), 'to': format_event_time(to_date), 'last_modified':
        format_event_time(last_modified), 'only_managed': only_managed,
        'include_managed': include_managed, 'include_deleted':
        include_deleted, 'include_moved': include_moved, 'include_geo':
        include_geo, 'localized_times': localized_times}).json()
    return Pages(self.request_handler, results, 'events', automatic_pagination)