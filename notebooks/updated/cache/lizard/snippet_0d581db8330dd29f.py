def work(request, slug):
    item = get_object_or_404(models.WorkBase.objects.visible(), slug=slug)
    if not item:
        raise Http404
    context = RequestContext(request, {'page': item, 'work': item})
    template = 'gk_collections/work.html'
    return TemplateResponse(request, template, context)