def current_site_id():
    if hasattr(override_current_site_id.thread_local, 'site_id'):
        return override_current_site_id.thread_local.site_id
    from yacms.utils.cache import cache_installed, cache_get, cache_set
    request = current_request()
    site_id = getattr(request, 'site_id', None)
    if request and not site_id:
        site_id = request.session.get('site_id', None)
        if not site_id:
            domain = request.get_host().lower()
            if cache_installed():
                bits = settings.CACHE_MIDDLEWARE_KEY_PREFIX, domain
                cache_key = '%s.site_id.%s' % bits
                site_id = cache_get(cache_key)
            if not site_id:
                try:
                    site = Site.objects.get(domain__iexact=domain)
                except Site.DoesNotExist:
                    pass
                else:
                    site_id = site.id
                    if cache_installed():
                        cache_set(cache_key, site_id)
    if not site_id:
        site_id = os.environ.get('YACMS_SITE_ID', settings.SITE_ID)
    if request and site_id and not getattr(settings, 'TESTING', False):
        request.site_id = site_id
    return site_id