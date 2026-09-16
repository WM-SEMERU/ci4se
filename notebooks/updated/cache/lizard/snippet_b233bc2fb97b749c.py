def get_occurrence(event_id, occurrence_id=None, year=None, month=None, day
    =None, hour=None, minute=None, second=None, tzinfo=None):
    if occurrence_id:
        occurrence = get_object_or_404(Occurrence, id=occurrence_id)
        event = occurrence.event
    elif None not in (year, month, day, hour, minute, second):
        event = get_object_or_404(Event, id=event_id)
        date = timezone.make_aware(datetime.datetime(int(year), int(month),
            int(day), int(hour), int(minute), int(second)), tzinfo)
        occurrence = event.get_occurrence(date)
        if occurrence is None:
            raise Http404
    else:
        raise Http404
    return event, occurrence