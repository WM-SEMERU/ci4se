def get_months(self, queryset=None, current_site=True):
    if queryset is None:
        queryset = self.get_queryset()
    if current_site:
        queryset = queryset.on_site()
    dates_qs = queryset.values_list(queryset.start_date_field, queryset.
        fallback_date_field)
    dates = []
    for blog_dates in dates_qs:
        if blog_dates[0]:
            current_date = blog_dates[0]
        else:
            current_date = blog_dates[1]
        dates.append((current_date.year, current_date.month))
    date_counter = Counter(dates)
    dates = set(dates)
    dates = sorted(dates, reverse=True)
    return [{'date': now().replace(year=year, month=month, day=1), 'count':
        date_counter[year, month]} for year, month in dates]