def this_year(self):
    start_date, end_date = get_date_range_this_year()
    return self.filter(start_time__gte=start_date, start_time__lte=end_date)