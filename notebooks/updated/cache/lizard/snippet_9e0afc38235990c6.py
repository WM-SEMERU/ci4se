def _get_weekly_date_range(self, metric_date, delta):
    dates = [metric_date]
    end_date = metric_date + delta
    spanning_years = end_date.year - metric_date.year
    for i in range(spanning_years):
        dates.append(datetime.date(year=metric_date.year + (i + 1), month=1,
            day=1))
    return dates