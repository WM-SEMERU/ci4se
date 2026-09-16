def publish_date(self, publish_date):
    self._group_data['publishDate'] = self._utils.format_datetime(publish_date,
        date_format='%Y-%m-%dT%H:%M:%SZ')