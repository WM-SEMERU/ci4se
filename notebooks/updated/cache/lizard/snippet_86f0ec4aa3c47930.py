def get_queryset(self, **options):
    days = options.get('days')
    queryset = TimelineLog.objects.order_by('-timestamp')
    if days:
        try:
            start = timezone.now() - timedelta(days=days)
        except TypeError:
            raise CommandError(
                "Incorrect 'days' parameter. 'days' must be a number of days.")
        else:
            return queryset.filter(timestamp__gte=start)
    return queryset