def __get_first_tuesday(this_date):
    month_range = calendar.monthrange(this_date.year, this_date.month)
    first_of_month = datetime.datetime(this_date.year, this_date.month, 1)
    first_tuesday_day = (calendar.TUESDAY - month_range[0]) % 7
    first_tuesday = first_of_month + datetime.timedelta(days=first_tuesday_day)
    return first_tuesday