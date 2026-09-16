def render(self, context, instance, placeholder):
    context = super(StatsGraphPlugin, self).render(context, instance,
        placeholder)
    limitMonthDates = {}
    for m in range(0, 25):
        limitMonthDates[m] = (timezone.now() - relativedelta(months=m)
            ).strftime('%Y-%m-%d')
    recentYears = [(timezone.now().year + x) for x in range(-5, 1)]
    series_by_year = Series.objects.order_by('year')
    if series_by_year.count() > 0:
        first_year = series_by_year.first().year
        allYears = [x for x in range(first_year, timezone.now().year + 1)]
    else:
        allYears = []
    context.update({'limitMonthDates': limitMonthDates, 'recentYears':
        recentYears, 'allYears': allYears})
    return context