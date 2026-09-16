def get_working_days_delta(self, start, end):
    start = cleaned_date(start)
    end = cleaned_date(end)
    if start == end:
        return 0
    if start > end:
        start, end = end, start
    count = 0
    while start < end:
        start += timedelta(days=1)
        if self.is_working_day(start):
            count += 1
    return count