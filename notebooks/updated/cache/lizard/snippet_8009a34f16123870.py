def on_site(self, site_id=None):
    if settings.PAGES_USE_SITE_ID:
        if not site_id:
            site_id = settings.SITE_ID
        return self.get_queryset().filter(sites=site_id)
    return self.all()