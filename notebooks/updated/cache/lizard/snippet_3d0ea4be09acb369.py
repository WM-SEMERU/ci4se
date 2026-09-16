def filter_queryset(self, request, queryset, view):
    if view.lookup_field not in view.kwargs:
        if not self.action_routing:
            return self.filter_list_queryset(request, queryset, view)
        else:
            method_name = 'filter_{action}_queryset'.format(action=view.action)
            return getattr(self, method_name)(request, queryset, view)
    return queryset