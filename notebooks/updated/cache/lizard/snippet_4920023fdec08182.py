def get_queryset(self, request):
    self.request = request
    qs = super(PublishingFluentPagesParentAdminMixin, self).get_queryset(
        request)
    qs = qs.filter(status=UrlNode.DRAFT)
    return qs