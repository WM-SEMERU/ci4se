def instance_from_url(url, user=None):
    from waldur_core.structure.managers import filter_queryset_for_user
    url = clear_url(url)
    match = resolve(url)
    model = get_model_from_resolve_match(match)
    queryset = model.objects.all()
    if user is not None:
        queryset = filter_queryset_for_user(model.objects.all(), user)
    return queryset.get(**match.kwargs)