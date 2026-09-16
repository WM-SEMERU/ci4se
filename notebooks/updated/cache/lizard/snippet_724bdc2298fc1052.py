def changelist_view(self, request, extra_context=None):
    if extra_context is None:
        extra_context = {}
    response = self.adv_filters_handle(request, extra_context=extra_context)
    if response:
        return response
    return super(AdminAdvancedFiltersMixin, self).changelist_view(request,
        extra_context=extra_context)