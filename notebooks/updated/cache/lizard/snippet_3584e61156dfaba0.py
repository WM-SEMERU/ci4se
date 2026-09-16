def save(self, *args, **kwargs):
    if not self.status:
        self.status = self.DRAFT
    if self.publication_date is None and self.status == self.PUBLISHED:
        self.publication_date = get_now()
    if self.status == self.DRAFT:
        if settings.PAGE_SHOW_START_DATE:
            if self.publication_date and self.publication_date <= get_now():
                self.publication_date = None
        else:
            self.publication_date = None
    self.last_modification_date = get_now()
    super(Page, self).save(*args, **kwargs)
    if settings.PAGE_HIDE_SITES and self.sites.count() == 0:
        self.sites.add(Site.objects.get(pk=global_settings.SITE_ID))