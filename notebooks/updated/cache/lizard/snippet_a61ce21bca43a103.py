def month_view(request, year, month, template='swingtime/monthly_view.html',
    queryset=None):
    year, month = int(year), int(month)
    cal = calendar.monthcalendar(year, month)
    dtstart = datetime(year, month, 1)
    last_day = max(cal[-1])
    dtend = datetime(year, month, last_day)
    queryset = queryset._clone(
        ) if queryset is not None else Occurrence.objects.select_related()
    occurrences = queryset.filter(start_time__year=year, start_time__month=
        month)

    def start_day(o):
        return o.start_time.day
    by_day = dict([(dt, list(o)) for dt, o in itertools.groupby(occurrences,
        start_day)])
    data = {'today': datetime.now(), 'calendar': [[(d, by_day.get(d, [])) for
        d in row] for row in cal], 'this_month': dtstart, 'next_month': 
        dtstart + timedelta(days=+last_day), 'last_month': dtstart +
        timedelta(days=-1)}
    return render(request, template, data)