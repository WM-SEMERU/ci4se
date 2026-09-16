def get_object(self, view_name, view_args, view_kwargs):
    lookup_value = view_kwargs[self.lookup_url_kwarg]
    kwargs = {self.lookup_url_kwarg: lookup_value}
    for parent_lookup_kwarg in list(self.parent_lookup_kwargs.keys()):
        lookup_value = view_kwargs[parent_lookup_kwarg]
        kwargs.update({self.parent_lookup_kwargs[parent_lookup_kwarg]:
            lookup_value})
    return self.get_queryset().get(**kwargs)