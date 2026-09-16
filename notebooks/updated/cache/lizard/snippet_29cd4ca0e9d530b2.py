def disposal_date(self):
    date_sampled = self.getDateSampled()
    if not date_sampled:
        return None
    retention_period = self.getSampleType().getRetentionPeriod() or {}
    retention_period_delta = timedelta(days=int(retention_period.get('days',
        0)), hours=int(retention_period.get('hours', 0)), minutes=int(
        retention_period.get('minutes', 0)))
    return dt2DT(DT2dt(date_sampled) + retention_period_delta)