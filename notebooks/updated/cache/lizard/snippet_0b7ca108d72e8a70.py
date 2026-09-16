def get_api_date(self):
    api_date = None
    if self.date is not None and not isinstance(self.date, datetime):
        try:
            api_date = datetime.strptime(self.date, '%Y-%m-%d')
        except (TypeError, ValueError):
            self.logger.warning("Invalid date '%s'", self.date)
    if api_date is None:
        utc_time = pytz.utc.localize(datetime.utcnow())
        eastern = pytz.timezone('US/Eastern')
        api_date = eastern.normalize(utc_time.astimezone(eastern))
        if api_date.hour < 10:
            api_date -= timedelta(days=1)
    self.date = api_date