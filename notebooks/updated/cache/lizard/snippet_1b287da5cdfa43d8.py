def slug(request, url):
    page = None
    if url:
        for slug in url.split('/'):
            if not slug:
                continue
            try:
                page = Page.objects.get(slug=slug, parent=page)
            except Page.DoesNotExist:
                raise Http404
    else:
        try:
            page = Page.objects.get(slug='index', parent=None)
        except Page.DoesNotExist:
            return TemplateView.as_view(template_name='wafer/index.html')(
                request)
    if 'edit' in request.GET:
        if not request.user.has_perm('pages.change_page'):
            raise PermissionDenied
        return EditPage.as_view()(request, pk=page.id)
    if 'compare' in request.GET:
        if not request.user.has_perm('pages.change_page'):
            raise PermissionDenied
        return ComparePage.as_view()(request, pk=page.id)
    return ShowPage.as_view()(request, pk=page.id)