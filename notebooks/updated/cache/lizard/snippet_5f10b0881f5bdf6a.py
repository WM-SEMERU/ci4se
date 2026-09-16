def reserve_time_slot(self, calendar_event, participant_id=None, **kwargs):
    from canvasapi.calendar_event import CalendarEvent
    calendar_event_id = obj_or_id(calendar_event, 'calendar_event', (
        CalendarEvent,))
    if participant_id:
        uri = 'calendar_events/{}/reservations/{}'.format(calendar_event_id,
            participant_id)
    else:
        uri = 'calendar_events/{}/reservations'.format(calendar_event_id)
    response = self.__requester.request('POST', uri, _kwargs=combine_kwargs
        (**kwargs))
    return CalendarEvent(self.__requester, response.json())