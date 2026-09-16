def get_site_url():
    site_url = getattr(_THREAD_LOCAL, _THREAD_SITE_URL, None)
    if site_url is None:
        site_url = SITE_URL or get_site_url_()
        setattr(_THREAD_LOCAL, _THREAD_SITE_URL, site_url)
    return site_url