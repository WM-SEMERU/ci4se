def create_date(past=False, max_years_future=10, max_years_past=10):
    if past:
        start = datetime.datetime.today() - datetime.timedelta(days=
            max_years_past * 365)
        num_days = max_years_future * 365 + start.day
    else:
        start = datetime.datetime.today()
        num_days = max_years_future * 365
    random_days = random.randint(1, num_days)
    random_date = start + datetime.timedelta(days=random_days)
    return random_date