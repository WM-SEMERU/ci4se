def serveDay(self, request, year=None, month=None, dom=None):
    myurl = self.get_url(request)
    today = timezone.localdate()
    if year is None:
        year = today.year
    if month is None:
        month = today.month
    if dom is None:
        dom = today.day
    year = int(year)
    month = int(month)
    dom = int(dom)
    day = dt.date(year, month, dom)
    eventsOnDay = self._getEventsOnDay(request, day)
    if len(eventsOnDay.all_events) == 1:
        event = eventsOnDay.all_events[0].page
        return redirect(event.get_url(request))
    monthlyUrl = myurl + self.reverse_subpage('serveMonth', args=[year, month])
    weekNum = gregorian_to_week_date(today)[1]
    weeklyUrl = myurl + self.reverse_subpage('serveWeek', args=[year, weekNum])
    listUrl = myurl + self.reverse_subpage('serveUpcoming')
    return render(request, 'joyous/calendar_list_day.html', {'self': self,
        'page': self, 'version': __version__, 'year': year, 'month': month,
        'dom': dom, 'day': day, 'monthlyUrl': monthlyUrl, 'weeklyUrl':
        weeklyUrl, 'listUrl': listUrl, 'monthName': MONTH_NAMES[month],
        'weekdayName': WEEKDAY_NAMES[day.weekday()], 'events': eventsOnDay})