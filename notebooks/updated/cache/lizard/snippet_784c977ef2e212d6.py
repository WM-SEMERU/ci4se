def calculate_date_strings(self, mode, numDays):
    yesterday = date.today() - timedelta(days=1)
    endday = datetime(yesterday.year, yesterday.month, yesterday.day, 23, 
        59, 59, 999)
    if mode:
        startday = yesterday - timedelta(days=numDays)
    else:
        startday = yesterday
    return startday.isoformat(), endday.strftime('%Y-%m-%d %H:%M:%S.%f')