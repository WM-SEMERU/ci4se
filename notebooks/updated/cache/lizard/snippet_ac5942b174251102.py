def site_info(request):
    site = get_current_site(request)
    context = {'WAFER_CONFERENCE_NAME': site.name,
        'WAFER_CONFERENCE_DOMAIN': site.domain}
    return context