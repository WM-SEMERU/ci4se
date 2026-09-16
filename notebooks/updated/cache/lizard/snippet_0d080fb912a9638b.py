def is_date(thing):
    date_types = datetime.datetime, datetime.date, DateTime
    return isinstance(thing, date_types)