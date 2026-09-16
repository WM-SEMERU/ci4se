def changelist_view(self, request, extra_context=None):
    extra_context = extra_context or {}
    if 'object' in request.GET.keys():
        value = request.GET['object'].split(':')
        content_type = get_object_or_404(ContentType, id=value[0])
        tracked_object = get_object_or_404(content_type.model_class(), id=
            value[1])
        extra_context['tracked_object'] = tracked_object
        extra_context['tracked_object_opts'] = tracked_object._meta
    return super(TrackingEventAdmin, self).changelist_view(request,
        extra_context)