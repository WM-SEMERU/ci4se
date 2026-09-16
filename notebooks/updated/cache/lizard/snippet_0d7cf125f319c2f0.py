def list_pages(self, request, template_name=None, extra_context=None):
    if not self.admin_site.has_permission(request):
        return self.admin_site.login(request)
    language = get_language_from_request(request)
    query = request.POST.get('q', '').strip()
    if query:
        page_ids = list(set([c.page.pk for c in Content.objects.filter(
            body__icontains=query)]))
        pages = Page.objects.filter(pk__in=page_ids)
    else:
        pages = Page.objects.root()
    if settings.PAGE_HIDE_SITES:
        pages = pages.filter(sites=settings.SITE_ID)
    context = {'can_publish': request.user.has_perm('pages.can_publish'),
        'language': language, 'name': _('page'), 'pages': pages, 'opts':
        self.model._meta, 'q': query}
    context.update(extra_context or {})
    change_list = self.changelist_view(request, context)
    return change_list