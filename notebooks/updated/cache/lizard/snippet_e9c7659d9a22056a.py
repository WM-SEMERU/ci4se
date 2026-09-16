def from_age_range(start_age, end_age):
    if start_age < 0 or end_age < 0:
        raise ValueError("start_age and end_age can't be negative")
    if start_age > end_age:
        start_age, end_age = end_age, start_age
    today = datetime.date.today()
    try:
        start_date = today.replace(year=today.year - end_age - 1)
    except ValueError:
        start_date = today.replace(year=today.year - end_age - 1, day=28)
    start_date += datetime.timedelta(days=1)
    try:
        end_date = today.replace(year=today.year - start_age)
    except ValueError:
        end_date = today.replace(year=today.year - start_age, day=28)
    date_range = DateRange(start_date, end_date)
    return DOB(date_range=date_range)