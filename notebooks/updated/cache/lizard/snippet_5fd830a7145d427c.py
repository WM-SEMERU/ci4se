def get_default_base_name(self, viewset):
    queryset = getattr(viewset, 'queryset', None)
    if queryset is not None:
        get_url_name = getattr(queryset.model, 'get_url_name', None)
        if get_url_name is not None:
            return get_url_name()
    return super(SortedDefaultRouter, self).get_default_base_name(viewset)