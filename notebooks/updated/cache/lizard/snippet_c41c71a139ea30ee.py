def post(self, request, *args, **kwargs):
    service_code = request.data['service_code']
    if service_code not in SERVICES.keys():
        return Response({'detail': _('Service not found')}, status=404)
    serializers = {'node': NodeRequestSerializer, 'vote':
        VoteRequestSerializer, 'comment': CommentRequestSerializer, 'rate':
        RatingRequestSerializer}
    kwargs['service_code'] = service_code
    kwargs['serializer'] = serializers[service_code]
    user = self.get_custom_data()
    request.UPDATED = request.data.copy()
    request.UPDATED['user'] = user['user']
    if service_code == 'node':
        for checkPOSTdata in ('layer', 'name', 'lat', 'long'):
            if checkPOSTdata not in request.data.keys():
                return Response({'detail': _(
                    'Mandatory parameter not found')}, status=400)
            elif not request.data[checkPOSTdata]:
                return Response({'detail': _(
                    'Mandatory parameter not found')}, status=400)
        layer = Layer.objects.get(slug=request.UPDATED['layer'])
        request.UPDATED['layer'] = layer.id
        lat = float(request.UPDATED['lat'])
        long = float(request.UPDATED['long'])
        point = Point((long, lat))
        request.UPDATED['geometry'] = point.wkt
        request.UPDATED['slug'] = slugify(request.UPDATED['name'])
    return self.create(request, *args, **kwargs)