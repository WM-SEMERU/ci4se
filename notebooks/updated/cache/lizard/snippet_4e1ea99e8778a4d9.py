def _create_date_slug(self):
    if not self.pk:
        d = utc_now()
    elif self.published and self.published_on:
        d = self.published_on
    elif self.updated_on:
        d = self.updated_on
    self.date_slug = '{0}/{1}'.format(d.strftime('%Y/%m/%d'), self.slug)