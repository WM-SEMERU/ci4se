def get(self, request, pzone_pk):
    try:
        pzone = PZone.objects.get(pk=pzone_pk)
    except PZone.DoesNotExist:
        raise Http404('Cannot find given pzone.')
    filters = {'pzone': pzone}
    if 'from' in request.GET:
        parsed = dateparse.parse_datetime(request.GET['from'])
        if parsed is not None:
            filters['when__gte'] = parsed
    if 'to' in request.GET:
        parsed = dateparse.parse_datetime(request.GET['to'])
        if parsed is not None:
            filters['when__lt'] = parsed
    operations = PZoneOperation.objects.filter(**filters)
    return Response(self.serialize_operations(operations), content_type=
        'application/json')