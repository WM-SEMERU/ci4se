def get(self, request, *args, **kwargs):
    try:
        year = int(self.kwargs.get('year'))
    except (ValueError, TypeError):
        year = getIntFromGet(request, 'year')
    if self.kwargs.get('month'):
        try:
            month = int(self.kwargs.get('month'))
        except (ValueError, TypeError):
            try:
                month = list(month_name).index(self.kwargs.get('month').title()
                    )
            except (ValueError, TypeError):
                month = None
    else:
        month = getIntFromGet(request, 'month')
    try:
        event_id = int(self.kwargs.get('event'))
    except (ValueError, TypeError):
        event_id = getIntFromGet(request, 'event')
    event = None
    if event_id:
        try:
            event = Event.objects.get(id=event_id)
        except ObjectDoesNotExist:
            pass
    kwargs.update({'year': year, 'month': month, 'startDate':
        getDateTimeFromGet(request, 'startDate'), 'endDate':
        getDateTimeFromGet(request, 'endDate'), 'basis': request.GET.get(
        'basis'), 'event': event})
    if kwargs.get('basis') not in EXPENSE_BASES.keys():
        kwargs['basis'] = 'accrualDate'
    context = self.get_context_data(**kwargs)
    return self.render_to_response(context)