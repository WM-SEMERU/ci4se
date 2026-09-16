def intersect_sites_method(form):
    if settings.PAGE_USE_SITE_ID:
        if settings.PAGE_HIDE_SITES:
            site_ids = [global_settings.SITE_ID]
        else:
            site_ids = [int(x) for x in form.data.getlist('sites')]

        def intersects_sites(sibling):
            return sibling.sites.filter(id__in=site_ids).count() > 0
    else:

        def intersects_sites(sibling):
            return True
    return intersects_sites