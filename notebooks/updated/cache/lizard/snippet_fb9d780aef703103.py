def get_absolute_url_with_date(self):
    pub_date = self.published_on
    if pub_date and settings.USE_TZ:
        pub_date = make_naive(pub_date, pytz.utc)
        pub_date = pytz.timezone(settings.TIME_ZONE).localize(pub_date)
    if pub_date:
        args = [pub_date.strftime('%Y'), pub_date.strftime('%m'), pub_date.
            strftime('%d'), self.slug]
    else:
        args = [self.slug]
    return reverse('blargg:entry_detail', args=args)