def _calendar_json_for_occurrence(self, occurrence):
    if occurrence.is_all_day:
        start = occurrence.start
        end = occurrence.start + timedelta(days=1)
    else:
        start = djtz.localize(occurrence.start)
        end = djtz.localize(occurrence.end)
    if occurrence.is_cancelled and occurrence.cancel_reason:
        title = '{0} [{1}]'.format(occurrence.event.title, occurrence.
            cancel_reason)
    else:
        title = occurrence.event.title
    if occurrence.event.primary_type:
        color = occurrence.event.primary_type.color
    else:
        color = '#cccccc'
    return {'title': title, 'allDay': occurrence.is_all_day or occurrence.
        event.contained_events.exists(), 'start': start, 'end': end, 'url':
        reverse('admin:icekit_events_eventbase_change', args=[occurrence.
        event.pk]), 'className': self._calendar_classes_for_occurrence(
        occurrence), 'backgroundColor': color}