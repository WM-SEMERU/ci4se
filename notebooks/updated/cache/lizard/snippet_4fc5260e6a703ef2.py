def stats(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    alerts_severities_count = queryset.values('severity').annotate(count=
        Count('severity'))
    severity_names = dict(models.Alert.SeverityChoices.CHOICES)
    alerts_severities_count = {severity_names[asc['severity']].lower(): asc
        ['count'] for asc in alerts_severities_count}
    for severity_name in severity_names.values():
        if severity_name.lower() not in alerts_severities_count:
            alerts_severities_count[severity_name.lower()] = 0
    return response.Response(alerts_severities_count, status=status.HTTP_200_OK
        )