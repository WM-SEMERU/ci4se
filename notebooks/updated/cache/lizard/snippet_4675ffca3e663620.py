def get_queryset(self, request):
    qs = super(VISADeviceAdmin, self).get_queryset(request)
    return qs.filter(protocol_id=PROTOCOL_ID)